from django.shortcuts import render, get_object_or_404
from .models import  Product 

# def home(request, category_slug=None):
#     category_page = None
#     products = None
#     if category_slug!=None:
#         category_page = get_object_or_404(Category, slug=category_slug)
#         products =  Product.objects.filter(category=category_page, available=True) 
#     else:
#         products = Product.objects.all().filter(available=True)
#     return render (request, 'home.html', {'category': category_page, 'product': products})

# def productPage(request):
#     return render (request, 'product.html')

def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home.html', context)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)