from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

import json
file = open(r'C:\Users\User\Desktop\Djanjo\car3\templates\car.json','r')

json_data=file.read()
temp=json.loads(json_data)
cars=temp["cars"]



def car1(request):
    context={
        'cars': cars 
    }
    return render(request,'home.html',context)

def car2(request,id):
    context={
        'car':cars[id - 1]
    }
    return render(request,'onecar.html',context)

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
