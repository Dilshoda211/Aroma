from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True)
    photo = models.ImageField(upload_to="Images/Users/",blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    def __str__(self):
        return f"{self.username} {self.phone_number}"


class Address(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="adresses")
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Adress"
        verbose_name_plural = "Adresses"
    
    def __str__(self):
        return f"{self.title} {self.user}"

