from django.shortcuts import render
from django.http import HttpResponse

"""
def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")
"""

def home(request):
    return render(request, 'home.html')
def contacts(request):
    return render(request, 'contact.html')
