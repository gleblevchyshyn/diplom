from django.db import models


class Author(models.Model):
    idauthor = models.AutoField(db_column='idAuthor', primary_key=True)  # Field name made lowercase.
    full_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'author'


class Book(models.Model):
    idbook = models.AutoField(db_column='idBook', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=80)
    average_rating = models.DecimalField(max_digits=2, decimal_places=1)
    description = models.TextField()
    isbn = models.CharField(max_length=45)
    num_pages = models.IntegerField(blank=True, null=True)
    publication_year = models.IntegerField()
    cover_img = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    ratings_count = models.IntegerField()
    amount = models.IntegerField()
    format_idformat = models.ForeignKey('Format', models.DO_NOTHING,
                                        db_column='Format_idFormat')  # Field name made lowercase.
    author_idauthor = models.ForeignKey(Author, models.DO_NOTHING,
                                        db_column='Author_idAuthor')  # Field name made lowercase.
    language_idlanguage = models.ForeignKey('Language', models.DO_NOTHING,
                                            db_column='Language_idLanguage')  # Field name made lowercase.
    publisher_idpublisher = models.ForeignKey('Publisher', models.DO_NOTHING,
                                              db_column='Publisher_idPublisher')  # Field name made lowercase.
    edition_information = models.CharField(max_length=100)
    is_ebook = models.IntegerField(blank=True, null=True)
    discount_iddiscount = models.ForeignKey('Discount', models.DO_NOTHING, db_column='Discount_idDiscount', blank=True,
                                            null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book'


class Bookhasgenres(models.Model):
    book_idbook = models.OneToOneField(Book, models.DO_NOTHING, db_column='Book_idBook',
                                       primary_key=True)  # Field name made lowercase. The composite primary key (Book_idBook, Genre_idGenre) found, that is not supported. The first column is selected.
    genre_idgenre = models.ForeignKey('Genre', models.DO_NOTHING,
                                      db_column='Genre_idGenre')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bookhasgenres'
        unique_together = (('book_idbook', 'genre_idgenre'),)


class Discount(models.Model):
    iddiscount = models.AutoField(db_column='idDiscount', primary_key=True)  # Field name made lowercase.
    type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'discount'


class Format(models.Model):
    idformat = models.AutoField(db_column='idFormat', primary_key=True)  # Field name made lowercase.
    format = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'format'


class Genre(models.Model):
    idgenre = models.AutoField(db_column='idGenre', primary_key=True)  # Field name made lowercase.
    genre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'genre'


class Language(models.Model):
    idlanguage = models.AutoField(db_column='idLanguage', primary_key=True)  # Field name made lowercase.
    language = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'language'


class Publisher(models.Model):
    idpublisher = models.AutoField(db_column='idPublisher', primary_key=True)  # Field name made lowercase.
    publisher = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'publisher'
