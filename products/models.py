from uuid import uuid4
from django.db import models


class Product(models.Model):

    CATEGORIES = [
        ('FO', 'Food'),
        ('DR', 'Drink'),
        ('DE', 'Dessert'),
        ('SA', 'Sauces')
    ]

    name = models.CharField(max_length=200)
    price = models.FloatField()
    offer_price = models.FloatField(null=True, blank=True)
    category = models.CharField(
        choices=CATEGORIES,
        default='FO',
        max_length=200
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/', null=True)

    class Meta:
        db_table = "products"