from django.db import models
from account.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return f"{self.name}"
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,related_name="products",null=True,blank=True)
    availability = models.BooleanField(default=True)
    main_descripton = models.TextField()
    descripton = models.TextField()
    image = models.ImageField(upload_to="Images/Products/")
    width = models.CharField(max_length=50, blank=True, null=True)
    height = models.CharField(max_length=50,blank=True, null=True)
    depth = models.CharField(max_length=50,blank=True, null=True)
    quality_checking = models.BooleanField(default=True)
    freshness_duration = models.CharField(max_length=50,blank=True, null=True)
    when_packeting = models.DateTimeField(blank=True, null=True)
    each_box_contains = models.CharField(max_length=50,blank=True, null=True)
    rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    
    def __str__(self):
        return f"{self.title} - {self.price}"


class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
                    models.UniqueConstraint(fields=["user", "product"], name="unique_user_product")
                ]
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"
    
    def __str__(self):
        return f"{self.user} - {self.product}"
    

class Review(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="reviews")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="reviews")
    comment = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
    def __str__(self):
        return f"{self.author.username} - {self.product.title}"