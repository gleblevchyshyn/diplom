# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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
    format_idformat = models.ForeignKey('Format', models.DO_NOTHING, db_column='Format_idFormat')  # Field name made lowercase.
    author_idauthor = models.ForeignKey(Author, models.DO_NOTHING, db_column='Author_idAuthor')  # Field name made lowercase.
    language_idlanguage = models.ForeignKey('Language', models.DO_NOTHING, db_column='Language_idLanguage')  # Field name made lowercase.
    publisher_idpublisher = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='Publisher_idPublisher')  # Field name made lowercase.
    edition_information = models.CharField(max_length=100)
    is_ebook = models.IntegerField(blank=True, null=True)
    discount_iddiscount = models.ForeignKey('Discount', models.DO_NOTHING, db_column='Discount_idDiscount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book'


class Bookhasgenres(models.Model):
    book_idbook = models.OneToOneField(Book, models.DO_NOTHING, db_column='Book_idBook', primary_key=True)  # Field name made lowercase. The composite primary key (Book_idBook, Genre_idGenre) found, that is not supported. The first column is selected.
    genre_idgenre = models.ForeignKey('Genre', models.DO_NOTHING, db_column='Genre_idGenre')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bookhasgenres'
        unique_together = (('book_idbook', 'genre_idgenre'),)


class Branch(models.Model):
    idbranch = models.AutoField(db_column='idBranch', primary_key=True)  # Field name made lowercase.
    n_branch = models.IntegerField()
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    deliverycompany_iddeliverycompany = models.ForeignKey('Deliverycompany', models.DO_NOTHING, db_column='DeliveryCompany_idDeliveryCompany')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'branch'


class Deliverycompany(models.Model):
    iddeliverycompany = models.AutoField(db_column='idDeliveryCompany', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'deliverycompany'


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


class Login(models.Model):
    idlogin = models.AutoField(db_column='idLogin', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    is_admin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login'


class Order(models.Model):
    idorder = models.AutoField(db_column='idOrder', primary_key=True)  # Field name made lowercase.
    delivery_date = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    orderstatus_idorderstatus = models.ForeignKey('Orderstatus', models.DO_NOTHING, db_column='OrderStatus_idOrderStatus')  # Field name made lowercase.
    branch_idbranch = models.ForeignKey(Branch, models.DO_NOTHING, db_column='Branch_idBranch')  # Field name made lowercase.
    payment_idpayment = models.ForeignKey('Payment', models.DO_NOTHING, db_column='Payment_idPayment')  # Field name made lowercase.
    order_date = models.DateField()
    user_iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='User_idUser')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class Orderitem(models.Model):
    amount = models.IntegerField()
    order_idorder = models.OneToOneField(Order, models.DO_NOTHING, db_column='Order_idOrder', primary_key=True)  # Field name made lowercase. The composite primary key (Order_idOrder, Book_idBook) found, that is not supported. The first column is selected.
    book_idbook = models.ForeignKey(Book, models.DO_NOTHING, db_column='Book_idBook')  # Field name made lowercase.
    is_recommended = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'orderitem'
        unique_together = (('order_idorder', 'book_idbook'),)


class Orderstatus(models.Model):
    idorderstatus = models.AutoField(db_column='idOrderStatus', primary_key=True)  # Field name made lowercase.
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'orderstatus'


class Payment(models.Model):
    idpayment = models.AutoField(db_column='idPayment', primary_key=True)  # Field name made lowercase.
    payment_way = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'payment'


class Publisher(models.Model):
    idpublisher = models.AutoField(db_column='idPublisher', primary_key=True)  # Field name made lowercase.
    publisher = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'publisher'


class Rewiev(models.Model):
    user_iduser = models.OneToOneField('User', models.DO_NOTHING, db_column='User_idUser', primary_key=True)  # Field name made lowercase. The composite primary key (User_idUser, Book_idBook) found, that is not supported. The first column is selected.
    book_idbook = models.ForeignKey(Book, models.DO_NOTHING, db_column='Book_idBook')  # Field name made lowercase.
    rating = models.IntegerField()
    text = models.CharField(max_length=300, blank=True, null=True)
    review_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rewiev'
        unique_together = (('user_iduser', 'book_idbook'),)


class User(models.Model):
    iduser = models.AutoField(db_column='idUser', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    login_idlogin = models.ForeignKey(Login, models.DO_NOTHING, db_column='Login_idLogin')  # Field name made lowercase.
    cashback = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'user'


class Wishlist(models.Model):
    book_idbook = models.OneToOneField(Book, models.DO_NOTHING, db_column='Book_idBook', primary_key=True)  # Field name made lowercase. The composite primary key (Book_idBook, User_idUser) found, that is not supported. The first column is selected.
    user_iduser = models.ForeignKey(User, models.DO_NOTHING, db_column='User_idUser')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wishlist'
        unique_together = (('book_idbook', 'user_iduser'),)
