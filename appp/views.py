from django.http import HttpResponse
from django.shortcuts import render
from appp.models import Contact
from django.contrib import messages


def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is website")

def about(request):
    #return HttpResponse("this is all about workouts")
    return render(request,'about.html')

def workout(request):
    #return HttpResponse("this is the list of workouts")
    return render(request,'workout.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact= Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'contact.html')

def chest(request):
    return render(request,'chest.html')
    #return HttpResponse("this is the chest plan")


def biceps(request):
    return render(request,'biceps.html')
    #return HttpResponse("this is the biceps plan")

def triceps(request):
    return render(request,'triceps.html')
    #return HttpResponse("this is the triceps plan")

def back(request):
    return render(request,'back.html')
    #return HttpResponse("this is the back plan")

def legs(request):
    return render(request,'legs.html')
    #return HttpResponse("this is the legs plan")

def cardio(request):
    return render(request,'cardio.html')
    #return HttpResponse("this is the cardio plan")

def exer(request):
    return render(request,'exer.html')
    #return HttpResponse("this is the exer plan")

def calves(request):
    return render(request,'calves.html')
    #return HttpResponse("this is the calves plan")

def hurt(request):
    return render(request,'hurt.html')
    #return HttpResponse("this is the hurt plan")
