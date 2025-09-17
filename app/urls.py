from django.urls import path
from .views import home_page,blog_page,category_page,checkout_page,confirmation_page,cart_page,contact_page,single_product_page,login_page,register_page,tracking_order_page

urlpatterns = [
    path('', home_page, name='home-page'),
    path('blog/', blog_page, name='blog-page'),
    path('category/', category_page, name='category-page'),
    path('checkout/', checkout_page, name='checkout-page'),
    path('confirmation/', confirmation_page, name='confirmation-page'),
    path('cart/', cart_page, name='cart-page'),
    path('contact/', contact_page, name='contact-page'),
    path('single-product/', single_product_page, name='single-product-page'),
    path('login/', login_page, name='login-page'),
    path('register/', register_page, name='register-page'),
    path('tracking-order/', tracking_order_page, name='tracking-order-page'),
]