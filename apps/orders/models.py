from django.db import models
from ..products.models import Book
from ..users.models import NewUser


class Branch(models.Model):
    idbranch = models.AutoField(db_column='idBranch', primary_key=True)  # Field name made lowercase.
    n_branch = models.IntegerField()
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    deliverycompany_iddeliverycompany = models.ForeignKey('Deliverycompany', models.RESTRICT, db_column='DeliveryCompany_idDeliveryCompany')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'branch'


class Deliverycompany(models.Model):
    iddeliverycompany = models.AutoField(db_column='idDeliveryCompany', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'deliverycompany'


class Order(models.Model):
    idorder = models.AutoField(db_column='idOrder', primary_key=True)  # Field name made lowercase.
    delivery_date = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    orderstatus_idorderstatus = models.ForeignKey('Orderstatus', models.RESTRICT, db_column='OrderStatus_idOrderStatus')  # Field name made lowercase.
    branch_idbranch = models.ForeignKey(Branch, models.RESTRICT, db_column='Branch_idBranch')  # Field name made lowercase.
    payment_idpayment = models.ForeignKey('Payment', models.RESTRICT, db_column='Payment_idPayment')  # Field name made lowercase.
    order_date = models.DateField()
    user_iduser = models.ForeignKey(NewUser, models.CASCADE, db_column='User_idUser')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'order'


class Orderitem(models.Model):
    amount = models.IntegerField()
    order_idorder = models.OneToOneField(Order, models.CASCADE, db_column='Order_idOrder', primary_key=True)  # Field name made lowercase. The composite primary key (Order_idOrder, Book_idBook) found, that is not supported. The first column is selected.
    book_idbook = models.ForeignKey(Book, models.CASCADE, db_column='Book_idBook')  # Field name made lowercase.
    is_recommended = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'orderitem'
        unique_together = (('order_idorder', 'book_idbook'),)


class Orderstatus(models.Model):
    idorderstatus = models.AutoField(db_column='idOrderStatus', primary_key=True)  # Field name made lowercase.
    status = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'orderstatus'


class Payment(models.Model):
    idpayment = models.AutoField(db_column='idPayment', primary_key=True)  # Field name made lowercase.
    payment_way = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'payment'