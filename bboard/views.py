from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb, User

def index(request):
    return render(request, 'index.html')



def index2(request):
    return render(request, 'index2.html')


def index3(request):
    return render(request, 'index3.html')