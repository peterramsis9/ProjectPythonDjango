from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product, Category

from .forms import ProductForm
# Create your views here.

def index(request):


    if request.method == 'POST':
        productForm = ProductForm(request.POST, request.FILES , category_queryset=Category.objects.all())
        if productForm.is_valid():
            productForm.save()
            context = {
                'message': 'Product added successfully!',
                'pform' : ProductForm(category_queryset=Category.objects.all()),
                "category": Category.objects.all(),
                'products': Product.objects.all(),
                 'success': True
            }
        else:
            context = {
                'products': Product.objects.all(),
                'pfrom': productForm,
                'category': Category.objects.all(),
                'form_errors': productForm.errors
            }
            
        
    else:
        products = Product.objects.all()
        categories = Category.objects.all()
       
        context = {
            'products': products,
            'categories': categories,
            'pform' : ProductForm(category_queryset=categories)
        }

    return render(request, 'pages/products.html', context)

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request,"pages/product.html", {'product': product})

   