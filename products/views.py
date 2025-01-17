
from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    return render(request,'home.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})


def transaction_complete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'transaction_complete.html', {'product': product})