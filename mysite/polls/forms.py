from email.mime import image
from django import forms


from django.conf import settings


# form person

class PersonForm(forms.Form):
    name = forms.CharField( required=True,label="Name", max_length=255,strip=True,min_length=2,widget=forms.TextInput(attrs={'type': 'text'}))
    sex = forms.ChoiceField(required=True,choices=[(x,y) for(x,y) in settings.SEXES],widget=forms.Select(attrs={'type': 'select'}))
    country = forms.ChoiceField(required=True,choices=[(x,y) for(x,y) in settings.COUNTRIES],widget=forms.Select(attrs={'type': 'select'}))
    age = forms.CharField( required=True, max_length=255,strip=True,min_length=2,widget=forms.TextInput(attrs={'type': 'number'}))

# form person

class MagasinForm(forms.Form):
    name = forms.CharField( required=True, max_length=255,strip=True,min_length=2,widget=forms.TextInput(attrs={'type': 'text'}))
    country = forms.ChoiceField(required=True,choices=[(x,y) for(x,y) in settings.COUNTRIES],widget=forms.Select(attrs={'type': 'select'}))
    
    
class ProfileMagasinForm(forms.Form):
    email = forms.EmailField(required=True,max_length=255,widget=forms.TextInput(attrs={'type': 'email'}))
    phone = forms.CharField( required=True, max_length=255,strip=True,min_length=2,widget=forms.TextInput(attrs={'type': 'number'}))
   
class ProduitForm(forms.Form):
    name = forms.CharField( required=True, max_length=255,strip=True,min_length=2,widget=forms.TextInput(attrs={'type': 'text'}))
    country = forms.ChoiceField(required=True,choices=[(x,y) for(x,y) in settings.COUNTRIES],widget=forms.Select(attrs={'type': 'select'}))
    price = forms.CharField( required=True, max_length=255,strip=True,min_length=2,widget=forms.TextInput(attrs={'type': 'number'}))
    image = forms.ImageField(required=True,)
   