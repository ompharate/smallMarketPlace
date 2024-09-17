from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        ordering = ('name',)
        return self.name
    
class item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='item_images', null=True, blank=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, null=True,related_name="items",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)