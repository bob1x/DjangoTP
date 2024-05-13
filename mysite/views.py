from django.shortcuts import render 
from django.template import loader 

def index1(request): 
    return render(request,'acceuil.html' )