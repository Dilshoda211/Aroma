from django.db import models
from account.models import User, Address
from product.models import Product
class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self):
        return self.user.username

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["cart", "product"], name="unique_cart_product")
        ]
        verbose_name = "Cart Item"
        verbose_name_plural = "Cart Items"
    
    def __str__(self):
        return f"{self.cart.user.username} {self.product.title} {self.quantity}"


class Order(models.Model):
     STATUS_CHOICES = [
         ("pending", "Pending"),
         ("shipped", "Shipped"),
         ("delivered", "Delivered"),
         ("cancelled", "Cancelled"),
     ]
     PAYMENT_STATUS_CHOICES = [
         ("pending", "Pending"),
         ("paid", "Paid"),
         ("failed", "Failed"),
     ]

     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
     address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
     payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default="pending")
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     class Meta:
         verbose_name = "Order"
         verbose_name_plural = "Orders"

     def __str__(self):
         return f"Order #{self.pk} - {self.user.username}"


class OrderItem(models.Model):
     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
     quantity = models.PositiveIntegerField(default=1)
     unit_price = models.DecimalField(max_digits=10, decimal_places=2)

     class Meta:
         verbose_name = "Order Item"
         verbose_name_plural = "Order Items"

     def __str__(self):
         return f"{self.product} x {self.quantity}"


# =======================
# Payment
# =======================
class Payment(models.Model):
     METHOD_CHOICES = [
         ("card", "Card"),
         ("cash", "Cash on Delivery"),
         ("paypal", "PayPal"),
     ]
     STATUS_CHOICES = [
         ("pending", "Pending"),
         ("completed", "Completed"),
         ("failed", "Failed"),
     ]

     order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
     amount = models.DecimalField(max_digits=10, decimal_places=2)
     method = models.CharField(max_length=20, choices=METHOD_CHOICES)
     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
     transaction_id = models.CharField(max_length=100, blank=True, null=True)
     created_at = models.DateTimeField(auto_now_add=True)

     class Meta:
         verbose_name = "Payment"
         verbose_name_plural = "Payments"

     def __str__(self):
         return f"Payment for Order #{self.order.pk}"
