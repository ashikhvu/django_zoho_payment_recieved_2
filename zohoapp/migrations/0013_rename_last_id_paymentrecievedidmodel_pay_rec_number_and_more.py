# Generated by Django 4.2.7 on 2023-11-26 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0012_alter_paymentrecievedmodel_acc_num_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentrecievedidmodel',
            old_name='last_id',
            new_name='pay_rec_number',
        ),
        migrations.AddField(
            model_name='paymentrecievedidmodel',
            name='ref_number',
            field=models.BigIntegerField(null=True),
        ),
    ]
