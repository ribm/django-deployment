from django.conf.urls import url 
from firstapp import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    
    
    path('index/', views.index)
    
]