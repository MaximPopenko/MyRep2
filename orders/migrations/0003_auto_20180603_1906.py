# Generated by Django 2.0.5 on 2018-06-03 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180603_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_adress',
            new_name='customer_address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='total_amount',
            new_name='total_price',
        ),
    ]