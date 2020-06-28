from django.contrib import admin
from django.urls import path
from . import views
from . import main

urlpatterns = [
	path('', views.home, name = 'home'), 
	path('search', main.main, name = 'nlp_search')

]