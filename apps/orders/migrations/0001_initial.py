# Generated by Django 4.2 on 2023-05-07 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('idbranch', models.AutoField(db_column='idBranch', primary_key=True, serialize=False)),
                ('n_branch', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'branch',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Deliverycompany',
            fields=[
                ('iddeliverycompany', models.AutoField(db_column='idDeliveryCompany', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'deliverycompany',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('idorder', models.AutoField(db_column='idOrder', primary_key=True, serialize=False)),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('order_date', models.DateField()),
                ('branch_idbranch', models.ForeignKey(db_column='Branch_idBranch', on_delete=django.db.models.deletion.RESTRICT, to='orders.branch')),
            ],
            options={
                'db_table': 'order',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Orderstatus',
            fields=[
                ('idorderstatus', models.AutoField(db_column='idOrderStatus', primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'orderstatus',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('idpayment', models.AutoField(db_column='idPayment', primary_key=True, serialize=False)),
                ('payment_way', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'payment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Orderitem',
            fields=[
                ('amount', models.IntegerField()),
                ('order_idorder', models.OneToOneField(db_column='Order_idOrder', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='orders.order')),
                ('is_recommended', models.IntegerField()),
            ],
            options={
                'db_table': 'orderitem',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='orderstatus_idorderstatus',
            field=models.ForeignKey(db_column='OrderStatus_idOrderStatus', on_delete=django.db.models.deletion.RESTRICT, to='orders.orderstatus'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_idpayment',
            field=models.ForeignKey(db_column='Payment_idPayment', on_delete=django.db.models.deletion.RESTRICT, to='orders.payment'),
        ),
    ]
