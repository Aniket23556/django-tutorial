# Views.py file for Assignment 2 view in views.py file

from django.shortcuts import render
from django.http import HttpResponse

def view1(request):
    # Your view1 logic here
    return HttpResponse("This is view 1")

def view2(request):
    # Your view2 logic here
    return HttpResponse("This is view 2")