from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name='about'),
    path('workout',views.workout,name='workout'),
    path('contact',views.contact,name='contact'),
    path('chest',views.chest,name='chest'),
    path('biceps',views.biceps,name='biceps'),
    path('triceps',views.triceps,name='triceps'),
    path('back',views.back,name='back'),
    path('legs',views.legs,name='legs'),
    path('cardio',views.cardio,name='cardio'),
    path('exer',views.exer,name='exer'),
    path('calves',views.calves,name='calves'),
    path('hurt',views.hurt,name='hurt')
]