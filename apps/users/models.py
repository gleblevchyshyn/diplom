from django.db import models
from ..products.models import Book


class Login(models.Model):
    idlogin = models.AutoField(db_column='idLogin', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    is_admin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login'


class Rewiev(models.Model):
    user_iduser = models.OneToOneField('User', models.DO_NOTHING, db_column='User_idUser',
                                       primary_key=True)  # Field name made lowercase. The composite primary key (User_idUser, Book_idBook) found, that is not supported. The first column is selected.
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
    book_idbook = models.OneToOneField(Book, models.DO_NOTHING, db_column='Book_idBook',
                                       primary_key=True)  # Field name made lowercase. The composite primary key (Book_idBook, User_idUser) found, that is not supported. The first column is selected.
    user_iduser = models.ForeignKey(User, models.DO_NOTHING, db_column='User_idUser')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wishlist'
        unique_together = (('book_idbook', 'user_iduser'),)
