# Generated by Django 4.2.7 on 2023-11-27 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0022_paymentrecievedmodel_paymentrecievedidmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentrecievedmodel',
            name='customer_gst_treatment',
            field=models.CharField(default='value', max_length=255),
        ),
    ]