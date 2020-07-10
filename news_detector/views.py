from django.shortcuts import render
from django.http import HttpResponse
from . import analyze

# Create your views here.
def home(request):
	return render(request, 'index.html')
def aboutus(request):
	return render(request, 'AboutUs.html')
def search(request):
	return render(request, 'Search.html')
def analyzer(request):
	analyze.function()
	return render(request, "analyze.html")
	