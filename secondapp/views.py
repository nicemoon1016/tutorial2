from django.shortcuts import render
from django.http import HttpResponse
from .models import Hospital

def hospital(request):
    curriculum = Hospital.objects.all()
    return render(request, 'show.html', {'list':curriculum})

def index10(request):
 return HttpResponse('<h1>Hello</h1>')

def index20(request):
 return HttpResponse('<h1>Hi</h1>')
