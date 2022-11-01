from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.







class MatrixDB(models.Model):
    m= models.CharField(max_length=5)
    m1 = models.CharField(max_length=5)
    m2= models.CharField(max_length=5)
    m3 = models.CharField(max_length=5)
    m4 = models.CharField(max_length=5)
    m5 = models.CharField(max_length=5)
    def __str__(self):
        return self.m1



class Nazvanie9models(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)