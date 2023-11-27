# Generated by Django 4.2.7 on 2023-11-26 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0014_remove_paymentrecievedmodel_bank_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentRecievedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_mail', models.EmailField(max_length=254, null=True)),
                ('customer_bill_address', models.TextField()),
                ('customer_gst_treatment', models.CharField(max_length=255)),
                ('customer_gst_number', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_recieved_number', models.CharField(max_length=255)),
                ('reference_number', models.CharField(max_length=255)),
                ('payment_recieved_date', models.DateTimeField(null=True)),
                ('payment_recieved_method', models.CharField(max_length=255)),
                ('cheque_id', models.CharField(blank=True, max_length=255, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=255, null=True)),
                ('acc_num', models.BigIntegerField(blank=True, null=True)),
                ('status', models.CharField(max_length=255, null=True)),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.bankcreation')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRecievedIdModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_number', models.BigIntegerField(null=True)),
                ('pay_rec_number', models.BigIntegerField(null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
