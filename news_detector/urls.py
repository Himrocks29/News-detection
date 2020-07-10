from django.contrib import admin
from django.urls import path
from . import views
from . import main
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	path('', views.home, name = 'Home'), 
	path('index.html', views.home, name='Home'),
	path('search', main.main, name = 'nlp_search'),
	path('AboutUs.html', views.aboutus, name = 'Intro'),
	path('Search.html', views.search, name = 'Verify News'), 
	path('analyse', views.analyzer, name = 'Admin Analyze')
	]

urlpatterns += staticfiles_urlpatterns() 