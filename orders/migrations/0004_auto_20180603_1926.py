# Generated by Django 2.0.5 on 2018-06-03 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180603_1906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Товар в заказе', 'verbose_name_plural': 'Товары в заказе'},
        ),
    ]
