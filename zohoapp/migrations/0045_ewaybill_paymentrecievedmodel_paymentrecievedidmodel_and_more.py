# Generated by Django 4.2.7 on 2023-12-03 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0044_remove_ewaybillidmodel_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EWayBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.CharField(blank=True, max_length=50, null=True)),
                ('transsub', models.CharField(blank=True, max_length=50, null=True)),
                ('customerzz', models.CharField(blank=True, max_length=100, null=True)),
                ('cemail', models.EmailField(blank=True, max_length=255, null=True)),
                ('cgst_trt_inp', models.CharField(blank=True, max_length=100, null=True)),
                ('cgstin_inp', models.CharField(blank=True, max_length=100, null=True)),
                ('invoiceno', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField()),
                ('trans', models.CharField(blank=True, max_length=100, null=True)),
                ('adda', models.TextField(blank=True, max_length=255, null=True)),
                ('addb', models.TextField(blank=True, max_length=255, null=True)),
                ('srcofsupply', models.CharField(blank=True, max_length=100, null=True)),
                ('transportation', models.CharField(blank=True, max_length=100, null=True)),
                ('km', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('vno', models.CharField(blank=True, max_length=50, null=True)),
                ('sub_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sgst', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cgst', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('igst', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('shipping_charge', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('adj', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('note', models.TextField(blank=True, max_length=255, null=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('cust', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRecievedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_mail', models.EmailField(max_length=254, null=True)),
                ('customer_bill_address', models.TextField()),
                ('customer_gst_treatment', models.CharField(blank=True, default='value', max_length=255)),
                ('customer_gst_number', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_recieved_number', models.CharField(max_length=255)),
                ('reference_number', models.CharField(max_length=255)),
                ('payment_recieved_date', models.DateTimeField(null=True)),
                ('payment_recieved_method', models.CharField(max_length=255)),
                ('cheque_id', models.CharField(blank=True, max_length=255, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=255, null=True)),
                ('acc_num', models.BigIntegerField(blank=True, null=True)),
                ('status', models.CharField(max_length=255, null=True)),
                ('pay_rec_amount', models.FloatField(blank=True, null=True)),
                ('pay_rec_paid', models.FloatField(blank=True, null=True)),
                ('pay_rec_balance', models.FloatField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='upload/')),
                ('file_comment', models.TextField(blank=True, null=True)),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.bankcreation')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRecievedIdModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_number', models.CharField(max_length=255, null=True)),
                ('pay_rec_number', models.CharField(max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRecievedComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer')),
                ('payment_recieved', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.paymentrecievedmodel')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRecievedAllInvoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('due_date', models.DateField(null=True)),
                ('invoice_type', models.CharField(max_length=255, null=True)),
                ('invoice_number', models.CharField(max_length=255, null=True)),
                ('invoice_amount', models.FloatField(blank=True, null=True)),
                ('paid', models.FloatField(blank=True, null=True)),
                ('balance', models.FloatField(blank=True, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer')),
                ('payment_recieved', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.paymentrecievedmodel')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EWayBillItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('eway_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.ewaybill')),
            ],
        ),
        migrations.CreateModel(
            name='EwaybillIdModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_number', models.CharField(max_length=255, null=True)),
                ('eway_bill_number', models.CharField(max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
