from django.shortcuts import render

from polls.models import *
from polls.forms import *

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)


# Create your views here.
def isMajeur(age :int) -> str : 
    return 'Majeur' if age >= 18 else 'Mineur'

def index(request,*args,**kwargs):
    template_name = 'index.html'
    # name = 'diakhou'
    # age = 18
    
    persons = person.objects.all()
    magasins = Magasin.objects.all()
    profileMagasins = ProfileMagasin.objects.all()
    produits = Produit.objects.all
    
    context = {'persons': persons,'magasins':magasins,'profileMagasins':profileMagasins ,'produits':produits} 
    return render(
        request = request, 
        template_name=template_name, 
        context=context
        )


def update_person(request,*args,**kwargs):
    template_name= 'update_person.html'
    
    obj = get_object_or_404(
        person,
        pk=kwargs.get('pk'),
    )
    if request.method == 'GET':
        form =PersonForm(
            initial={
                'name': obj.name,
                'age': obj.age,
            }
        )
        context = {
            'form': form,
        }
        return render(request=request,template_name=template_name,context=context,)
    
    if request.method == 'POST':
        form =PersonForm(
           request.POST,
           request.FILES,
           initial={
                'name': obj.name,
                'age': obj.age,
            }
        )
        context = {
            'form': form,
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data['name']
            obj.age = form.cleaned_data['age']
            obj.sex = form.cleaned_data['sex']
            obj.country = form.cleaned_data['country']
            obj.save()    
            return redirect('home')
        return render(request=request,template_name=template_name,context=context,)

def update_magasin(request,*args,**kwargs):
    template_name= 'update_magasin.html'
    
    obj = get_object_or_404(
        Magasin,
        pk=kwargs.get('pk'),
    )
    if request.method == 'GET':
        form =MagasinForm(
            initial={
                'name': obj.name,
                'country': obj.country,
            }
        )
        context = {
            'form': form,
        }
        return render(request=request,template_name=template_name,context=context,)
    
    if request.method == 'POST':
        form =MagasinForm(
           request.POST,
           request.FILES,
           initial={
                'name': obj.name,
                'country': obj.country,
            }
        )
        context = {
            'form': form,
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data['name']
            obj.country = form.cleaned_data['country']
           
            obj.save()    
            return redirect('home')
        return render(request=request,template_name=template_name,context=context,)
    
def update_profileMagasin(request,*args,**kwargs):
    template_name= 'update_profileMagasin.html'
    
    obj = get_object_or_404(
        ProfileMagasin,
        pk=kwargs.get('pk'),
    )
    if request.method == 'GET':
        form =ProfileMagasinForm(
            initial={
                'email': obj.email,
                'phone': obj.phone,
            }
        )
        context = {
            'form': form,
        }
        return render(request=request,template_name=template_name,context=context,)
    
    if request.method == 'POST':
        form =ProfileMagasinForm(
           request.POST,
           request.FILES,
           initial={
                'email': obj.email,
                'phone': obj.phone,
            }
        )
        context = {
            'form': form,
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.email = form.cleaned_data['email']
            obj.phone = form.cleaned_data['phone']
          
            obj.save()    
            return redirect('home')
        return render(request=request,template_name=template_name,context=context,)

def update_produit(request,*args,**kwargs):
    template_name= 'update_produit.html'
    
    obj = get_object_or_404(
        Produit,
        pk=kwargs.get('pk'),
    )
    if request.method == 'GET':
        form =ProduitForm(
            initial={
                'name': obj.name,
                'country': obj.country,
                'price': obj.price,
                'image': obj.image,
            }
        )
        context = {
            'form': form,
        }
        return render(request=request,template_name=template_name,context=context,)
    
    if request.method == 'POST':
        form =ProduitForm(
           request.POST,
           request.FILES,
           initial={
                'name': obj.name,
                'country': obj.country,
                'price': obj.price,
                'image': obj.image,
            }
        )
        context = {
            'form': form,
        }
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data['name']
            obj.country = form.cleaned_data['country']
            obj.price = form.cleaned_data['price']
            obj.image = form.cleaned_data['image']
          
            obj.save()    
            return redirect('home')
        return render(request=request,template_name=template_name,context=context,)


