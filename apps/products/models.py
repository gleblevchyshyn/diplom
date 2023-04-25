from django.db import models


class Author(models.Model):
    idauthor = models.AutoField(db_column='idAuthor', primary_key=True)  # Field name made lowercase.
    full_name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'author'


class Book(models.Model):
    idbook = models.AutoField(db_column='idBook', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=255)
    average_rating = models.DecimalField(max_digits=2, decimal_places=1)
    description = models.TextField()
    isbn = models.CharField(max_length=13)
    num_pages = models.IntegerField(blank=True, null=True)
    publication_year = models.IntegerField()
    cover_img = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    ratings_count = models.IntegerField()
    amount = models.IntegerField()
    language_idlanguage = models.ForeignKey('Language', models.RESTRICT,
                                            db_column='Language_idLanguage')  # Field name made lowercase.
    edition_information = models.CharField(max_length=250)
    is_ebook = models.IntegerField(blank=True, null=True)
    discount_iddiscount = models.ForeignKey('Discount', models.SET_NULL, db_column='Discount_idDiscount', blank=True,
                                            null=True)  # Field name made lowercase.
    publisher = models.CharField(max_length=250)
    format_idformat = models.ForeignKey('Format', models.RESTRICT,
                                        db_column='Format_idFormat')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'book'


class Bookhasauthor(models.Model):
    author_idauthor = models.OneToOneField(Author, models.CASCADE, db_column='Author_idAuthor',
                                           primary_key=True)  # Field name made lowercase. The composite primary key (Author_idAuthor, Book_idBook) found, that is not supported. The first column is selected.
    book_idbook = models.ForeignKey(Book, models.CASCADE, db_column='Book_idBook')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'bookhasauthor'
        unique_together = (('author_idauthor', 'book_idbook'),)


class Bookhasgenres(models.Model):
    book_idbook = models.OneToOneField(Book, models.CASCADE, db_column='Book_idBook',
                                       primary_key=True)  # Field name made lowercase. The composite primary key (Book_idBook, Genre_idGenre) found, that is not supported. The first column is selected.
    genre_idgenre = models.ForeignKey('Genre', models.CASCADE,
                                      db_column='Genre_idGenre')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'bookhasgenres'
        unique_together = (('book_idbook', 'genre_idgenre'),)


class Discount(models.Model):
    iddiscount = models.AutoField(db_column='idDiscount', primary_key=True)  # Field name made lowercase.
    type = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'discount'


class Format(models.Model):
    idformat = models.IntegerField(db_column='idFormat', primary_key=True)  # Field name made lowercase.
    format = models.CharField(max_length=110)

    class Meta:
        managed = True
        db_table = 'format'


class Genre(models.Model):
    idgenre = models.AutoField(db_column='idGenre', primary_key=True)  # Field name made lowercase.
    genre = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'genre'


class Language(models.Model):
    idlanguage = models.AutoField(db_column='idLanguage', primary_key=True)  # Field name made lowercase.
    language = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'language'
