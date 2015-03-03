from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

#This is the First Page's view.
def index(request):
    return HttpResponse("Gym Manager System")