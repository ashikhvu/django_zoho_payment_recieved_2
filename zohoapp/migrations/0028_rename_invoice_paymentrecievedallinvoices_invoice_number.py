# Generated by Django 4.2.7 on 2023-11-30 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0027_paymentrecievedallinvoices_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentrecievedallinvoices',
            old_name='invoice',
            new_name='invoice_number',
        ),
    ]