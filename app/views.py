from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
def home_page(request):
    return render(request=request,template_name="index.html")

def blog_page(request):
    return render(request=request,template_name="blog.html")

def category_page(request):
    return render(request=request,template_name="category.html")

def checkout_page(request):
    return render(request=request,template_name="checkout.html")

def confirmation_page(request):
    return render(request=request,template_name="confirmation.html")

def cart_page(request):
    return render(request=request,template_name="cart.html")

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Murojatingiz muvaffaqiyatli yuborildi  🎉")
            return redirect('home-page')
    return render(request=request,template_name='contact.html')

def single_product_page(request):
    return render(request=request,template_name="single-product.html")

def login_page(request):
    return render(request=request,template_name="login.html")

def register_page(request):
    return render(request=request,template_name="register.html")

def tracking_order_page(request):
    return render(request=request,template_name="tracking-order.html")