from django.urls import reverse
import email
from django.db import models

from django.conf import settings

# Create your models here.

# person
class person(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255,choices=settings.SEXES)
    country = models.CharField(max_length=255)
    age = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.name
    
    @property
    def isMajeur(age :int) -> str : 
        return 'Majeur' if age >= 18 else 'Mineur'
    
    def get_update_url(self):
        return reverse('update',kwargs={'pk':self.id})
        
    
# description name country created at 
class Description(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200,choices=settings.COUNTRIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    class Meta:
        abstract = True
        ordering = ('name',)

# magasin
class Magasin(Description):
    
    def get_update_url(self):
        return reverse('updateM',kwargs={'pk':self.id})

#profile magasin
class ProfileMagasin(models.Model):
    email = models.EmailField(max_length=200,unique=True)
    phone = models.CharField(max_length=30,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    magasin = models.OneToOneField(Magasin,on_delete=models.CASCADE,related_name="magasin_profile")
    
    def get_update_url(self):
        return reverse('updatePM',kwargs={'pk':self.id})

# Produit
class Produit(Description):
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to="PRODUCT_IMG")
    magasin = models.ForeignKey(Magasin,on_delete=models.CASCADE,related_name="produit_magasin")
    
    def get_update_url(self):
        return reverse('updateProduit',kwargs={'pk':self.id})
