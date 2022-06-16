import random

from django.shortcuts import get_object_or_404, render
from .models import Product

def index(request):
    template_name = 'index.html'

    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, template_name, context)

def product(request, product_id):

    product = get_object_or_404(Product,pk=product_id)

    if product:
        related_products = Product.objects\
            .filter(category=product.category)\
            .exclude(id=product.id).order_by('?')[0:4]

    context = {
        'product': product,
        'related_products': related_products
    }

    template_name = 'product.html'
    return render(request, template_name, context)