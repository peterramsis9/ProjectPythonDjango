from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
# Create your views here.

def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'pages/products.html' , context)


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request,"pages/product.html", {'product': product})

   