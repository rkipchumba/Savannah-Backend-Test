# Generated by Django 4.2.10 on 2024-02-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers_orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
