# Generated by Django 4.2.7 on 2023-12-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0048_ewaycomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='ewaybillidmodel',
            name='pattern',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='paymentrecievedidmodel',
            name='pattern',
            field=models.CharField(max_length=255, null=True),
        ),
    ]