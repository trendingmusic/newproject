from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def index(request):
    return HttpResponse('index')
