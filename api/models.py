from django.db import models

# Create your models here.
class Library(models.Model):
    name=models.CharField(max_length=100, blank=False, null=False)
    price=models.PositiveIntegerField(blank=True, default=0)
    author=models.CharField(max_length=300)
    pages=models.PositiveIntegerField(default=0)
    created_date=models.DateField(auto_now_add=True)
    created_at=models.TimeField(auto_now_add=True)
    updated_at=models.TimeField(auto_now=True)

    def __str__(self):
        return self.name