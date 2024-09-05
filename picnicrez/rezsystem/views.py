from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def FAQ(request):
    return render(request, 'FAQ.html')

def rules(request):
    return render(request, 'rules.html')

def maps(request):
    return render(request, 'maps.html')