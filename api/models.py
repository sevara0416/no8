from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class CustomUser(AbstractUser):
    name=models.CharField(max_length=50, blank=False, null=False)
    age=models.PositiveIntegerField(default=18)
    phone_number=models.CharField(max_length=50, blank=False)

class Library(models.Model):
    name=models.CharField(max_length=100, blank=False, null=False)
    price=models.PositiveIntegerField(blank=True, default=0)
    author=models.CharField(max_length=300)
    pages=models.PositiveIntegerField(default=50)
    created_date=models.DateField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


