from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def calculate(request):
    return render(request, 'calculate.html')
