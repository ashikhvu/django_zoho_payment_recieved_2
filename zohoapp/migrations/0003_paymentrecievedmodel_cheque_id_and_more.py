# Generated by Django 4.2.7 on 2023-11-25 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0002_paymentrecievedmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentrecievedmodel',
            name='cheque_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='paymentrecievedmodel',
            name='upi_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
