# Generated by Django 4.2.7 on 2023-11-26 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0009_paymentrecievedmodel_paymentrecievedidmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentrecievedidmodel',
            old_name='my_id',
            new_name='last_id',
        ),
    ]