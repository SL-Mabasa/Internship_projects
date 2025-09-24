from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Product
from .forms import CustomUserCreationForm

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def cart(request):
    cart_items = request.session.get('cart', {})
    products = []
    total = 0
    for product_id, quantity in cart_items.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * quantity
        total += subtotal
        products.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
    return render(request, 'cart.html', {'products': products, 'total': total})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    qty = int(request.POST.get('quantity', 1))
    cart[str(product_id)] = cart.get(str(product_id), 0) + qty
    request.session['cart'] = cart
    return redirect('cart')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors) 
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})