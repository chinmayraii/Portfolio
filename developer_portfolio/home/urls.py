from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('start_quiz',views.start_quiz),
    path('main_quiz',views.main_quiz),
    path('cal',views.cal),
    path('resume',views.resume),
    path('contact',views.contact),
    path('contact_light',views.contact_light),
    path('light',views.light),
]