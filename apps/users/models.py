from django.contrib.auth.models import AbstractUser
from django.db import models
from ..products.models import Book


class NewUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    phone = models.CharField(max_length=15)
    cashback = models.DecimalField(max_digits=9, decimal_places=2)


class Rewiev(models.Model):
    user_iduser = models.OneToOneField(NewUser, models.CASCADE, db_column='User_idUser', primary_key=True)  # Field name made lowercase. The composite primary key (Customer_idCustomer, Book_idBook) found, that is not supported. The first column is selected.
    book_idbook = models.ForeignKey(Book, models.CASCADE, db_column='Book_idBook')  # Field name made lowercase.
    rating = models.IntegerField()
    text = models.CharField(max_length=300, blank=True, null=True)
    review_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'rewiev'
        unique_together = (('user_iduser', 'book_idbook'),)


class Wishlist(models.Model):
    book_idbook = models.OneToOneField(Book, models.CASCADE, db_column='Book_idBook', primary_key=True)  # Field name made lowercase. The composite primary key (Book_idBook, Customer_idCustomerr) found, that is not supported. The first column is selected.
    user_iduser = models.ForeignKey(NewUser, models.CASCADE, db_column='User_idUser')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'wishlist'
        unique_together = (('book_idbook', 'user_iduser'),)
