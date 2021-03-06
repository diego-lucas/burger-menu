# Generated by Django 4.0.5 on 2022-06-09 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('offer_price', models.FloatField(blank=True)),
                ('category', models.CharField(choices=[('FO', 'Food'), ('DR', 'Drink'), ('DE', 'Dessert'), ('SA', 'Sauces')], default='FO', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='uploads/')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
