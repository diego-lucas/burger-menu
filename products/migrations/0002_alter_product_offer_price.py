# Generated by Django 4.0.5 on 2022-06-09 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='offer_price',
            field=models.FloatField(),
        ),
    ]