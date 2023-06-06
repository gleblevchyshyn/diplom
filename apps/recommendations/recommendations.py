import pandas as pd
import numpy as np
import string
import nltk.corpus as corpus
from nltk.stem import WordNetLemmatizer
import re
import gensim.downloader as api
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from surprise import SVD
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate


class RecommendationSystems:
    def __init__(self):
        self.books = pd.read_csv('processed_books.csv')
        self.books['author_ids'] = self.books['author'].apply(lambda x: ';'.join(str(i) for i in eval(x)))
        self.reviews = pd.DataFrame()

        self.tfidf_matrix = self.tf_idf_vectorization()
        self.unique_book_ids = self.train_svd_model()
        self.data = None
        self.algo = None

        self.top_100_books_ids = self.top_100_books()

        self.lemmatizer = WordNetLemmatizer()
        self.stopwords = corpus.stopwords.words('english')

        self.glove = api.load("glove-wiki-gigaword-300")
        self.embeddings = None



    def clean_text(self, text):
        # Convert to lowercase
        text = text.lower()
        # Remove URLs
        text = re.sub(r'http\S+', '', text)
        # Remove HTML tags
        text = re.sub(r'<.*?>', '', text)
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Remove numbers
        text = re.sub(r'\d+', '', text)
        # Tokenize into words
        words = text.split()
        text = ' '.join([self.lemmatizer.lemmatize(w) for w in words if not w in self.stopwords])
        return text

    def clean_text_column(self, column_name):
        if column_name in self.books.columns:
            self.books[f'processed_{column_name}'] = self.books[column_name].apply(lambda x: self.clean_text(x))
            return True
        return False

    # RECOMMENDATION SYSTEM BUILD ON GLOVE
    # Define a function to convert a string into GloVe embeddings
    def string_to_glove(self, line):
        # Tokenize the string into words
        tokens = line.lower().split()
        # Look up the GloVe embedding for each word
        embeddings = [self.glove.get_vector(word) for word in tokens if word in self.glove.key_to_index]
        # Combine the embeddings into a single vector
        if len(embeddings) > 0:
            glove = np.mean(embeddings, axis=0)
        else:
            glove = np.zeros(self.glove.vector_size)
        return glove

    def column_to_glove(self, column_name):
        if column_name in self.books.columns:
            self.books[f'glove_{column_name}'] = self.books[f'processed_{column_name}'].apply(
                lambda x: self.string_to_glove(x))
            if column_name == 'glove_description':
                self.embeddings = np.array(self.books['glove_description'].tolist())
            return True
        return False

    def search(self, query):
        processed = re.sub("[^a-zA-Z0-9 ]", "", query.lower())
        query_vec = self.string_to_glove(processed).reshape(1, -1)
        similarity = cosine_similarity(query_vec, self.embeddings).flatten()
        indices = np.argpartition(similarity, -50)[-50:]
        results = self.books.iloc[indices]
        return indices, results

    # COLLABORATIVE FILTERING RECOMMENDATION SYSTEM
    def cross_validate_svd_model(self, cv=5):
        # Load the data
        reader = Reader(rating_scale=(1, 5))
        self.data = Dataset.load_from_df(self.reviews[['user_id', 'book_id', 'rating']], reader)

        # Define the algorithm
        self.algo = SVD()

        # Evaluate the algorithm using 5-fold cross-validation
        results = cross_validate(self.algo, self.data, measures=['RMSE'], cv=cv, verbose=True)

        # Print the mean RMSE score
        print('Mean RMSE:', results['test_rmse'].mean())

        return results

    def train_svd_model(self):
        results = self.cross_validate_svd_model()
        trainset = self.data.build_full_trainset()
        self.algo.fit(trainset)

        # Retrieve all book IDs from the dataset
        all_book_ids = trainset.raw_ratings[:, 1]
        return set(all_book_ids)

    def predict(self, user_id=None):
        # Create a list to store the predicted ratings for each book
        predictions = []

        # Iterate over all book IDs and make predictions for the user
        for book_id in self.unique_book_ids:
            prediction = self.algo.predict(user_id, book_id)
            predictions.append((book_id, prediction.est))

        # Sort the predictions based on the estimated ratings in descending order
        predictions.sort(key=lambda x: x[1], reverse=True)

        # Retrieve the top 10 predicted books
        top_10_books = predictions[:10]

        # Return the list of top 10 book IDs
        return [book_id for book_id, _ in top_10_books]

    # CONTENT-BASED COLLABORATIVE FILTERING
    def tf_idf_vectorization(self):
        # define the features to be included in the TF-IDF matrix
        features = ['processed_description', 'author_ids', 'publisher', 'format', 'language_code', 'title', 'num_pages',
                    'publication_year']

        self.books['text'] = self.books['title'] + ' ' + self.books['processed_description'] + ' ' + self.books[
            'author_ids'] + ' ' + self.books[
                                 'publisher'] + ' ' + self.books['format'] + ' ' + self.books['language_code'] + ' ' + \
                             self.books['num_pages'].astype(
                                 str) + ' ' + self.books['publication_year'].astype(str)

        # initialize the vectorizer
        tfidf = TfidfVectorizer()

        # fit and transform the text data
        tfidf_matrix = tfidf.fit_transform(self.books['text'])
        return tfidf_matrix

    def get_similar_books(self, book_id, num_books=20):
        # get the index of the given book
        idx = self.books[self.books['book_id'] == book_id].index

        # calculate the cosine similarity between the given book and all other books
        cosine_sim = cosine_similarity(self.tfidf_matrix[idx], self.tfidf_matrix)

        # get the cosine similarity scores between the given book and all other books
        sim_scores = list(enumerate(cosine_sim[0]))

        # sort the scores in descending order
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # get the indices of the top similar books
        sim_indices = [i[0] for i in sim_scores[1:num_books + 1]]

        return sim_indices

    # Top Books
    def top_100_books(self):
        R = self.books['average_rating']
        v = self.books['ratings_count']
        m = self.books['ratings_count'].quantile(0.7)
        C = self.books['average_rating'].mean()

        self.books['Weighted_average_rating'] = (R * v + C * m) / (v + m)

        # Sort the dataframe by weighted average rating in descending order
        sorted_df = self.books.sort_values('Weighted_average_rating', ascending=False)

        # Get the indices of the top 100 books
        top_100_indices = sorted_df.head(100).index

        return top_100_indices
