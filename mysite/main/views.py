from django.shortcuts import render, redirect
from .models import (HomeName, HomeImage, 
                    Contact, About, 
                    Product, Cart)
# Create your views here.

def home(request):
    home_name = HomeName.objects.all()[0]
    home_image = HomeImage.objects.all()
    cart_list = Cart.objects.all()

    return render(request, 'main/home.html', context={
       'home_name':home_name ,
       'home_image':home_image,
        'cart_list':cart_list

    })

def about(request):
    about_info = About.objects.all()[0]
    cart_list = Cart.objects.all()

    return render(request, 'main/about.html', context={'about_info':about_info,
        'cart_list':cart_list
     })


def contact(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        review = request.POST.get('review')
        Contact.objects.create(username=username, email=email, review=review)
        return redirect('home')
    cart_list = Cart.objects.all()

    return render(request, 'main/contact.html', context={
        'cart_list':cart_list
        
    })


def review(request):
    review_list = Contact.objects.all()
    cart_list = Cart.objects.all()

    return render(request, 'main/review.html', context={
        'review_list':review_list,
        'cart_list':cart_list

    })


def product(request):
    product_list = Product.objects.all()
    cart_list = Cart.objects.all()

    return render(request, 'main/products.html', context={
        'product_list':product_list,
        'cart_list':cart_list

    })

def product_detail(request, id):
    my_prod = Product.objects.get(pk=id)
    return render(request, 'main/product_detail.html', context={
        'my_prod':my_prod
    })

def cart(request):
    summ = 0
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        my_prod = Product.objects.get(id=prod_id)
        Cart.objects.create(prod_item=my_prod)
        return redirect('product')
    cart_list = Cart.objects.all()
    for i in cart_list:
        summ += i.prod_item.price
    return render(request, 'main/cart.html', context={
        'cart_list':cart_list,
        'summ':summ
    })


def detele_product(request):
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        Cart.objects.filter(id=prod_id).delete()
        return redirect('cart')  