from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')