from django.shortcuts import render
from django.http import HttpResponse
from .models import Hospital

def hospital(request):
    hospital = Hospital.objects.all()
    print(hospital)
    return render(request, 'hospital.html', {'list':hospital})
