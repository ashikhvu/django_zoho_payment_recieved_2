# Generated by Django 4.2.7 on 2023-11-25 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0005_paymentrecievedmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentrecievedmodel',
            name='acc_num',
            field=models.BigIntegerField(null=True),
        ),
    ]
