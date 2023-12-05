# Generated by Django 4.2.7 on 2023-12-03 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0045_ewaybill_paymentrecievedmodel_paymentrecievedidmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportation',
            name='type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transportation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]