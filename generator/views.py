from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    length = int(request.GET.get('length'))
    characters = list("abcdefghijklmnopqrstuvwxyz")

    the_password = ""

    if request.GET.get('uppercase'):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))

    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*()"))


    for x in range(length):
        the_password += random.choice(characters)


    return render(request, 'generator/password.html', { "password": the_password})

def about(request):
    return render(request,'generator/about.html')