# Generated by Django 4.2.7 on 2023-11-26 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0020_paymentrecievedmodel_paymentrecievedidmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentrecievedmodel',
            name='bank',
        ),
        migrations.RemoveField(
            model_name='paymentrecievedmodel',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='paymentrecievedmodel',
            name='user',
        ),
        migrations.DeleteModel(
            name='PaymentRecievedIdModel',
        ),
        migrations.DeleteModel(
            name='PaymentRecievedModel',
        ),
    ]
