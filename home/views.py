from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h4>Hello, world</h4>')
