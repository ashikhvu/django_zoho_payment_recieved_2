# Generated by Django 4.2.7 on 2023-12-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0050_paymentrecievedallinvoices_invoice_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentrecievedmodel',
            name='pdf_to_send',
            field=models.FileField(blank=True, null=True, upload_to='upload/'),
        ),
    ]
