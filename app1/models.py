from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=(
        ('chef', 'chef'),
        ('viewer', 'viewer')
    ))
    
class Recipe(models.Model):
    cus_rec = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id = models.AutoField
    name = models.CharField(max_length=50)
    ing = models.TextField(max_length=500)
    cook = models.TextField(max_length=500)
    cat = models.CharField(max_length=20, choices=(
        ('soup','soup'),
        ('starters','starters'),
        ('main course', 'main course'),
        ('dessert','dessert')
    ))
    img = models.ImageField(upload_to='chef')
    
class fav(models.Model):
    rec_fav = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    
class Comments(models.Model):
    rec_comment = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    com = models.CharField(max_length=20)
    author = models.CharField(max_length=20)