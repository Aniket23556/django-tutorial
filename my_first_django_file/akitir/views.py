# Views.py file for "Assignment 2" view in views.py file

# from django.shortcuts import render
# from django.http import HttpResponse

# def view1(request):
#     # Your view1 logic here
#     return HttpResponse("This is view 1")

# def view2(request):
#     # Your view2 logic here
#     return HttpResponse("This is view 2")


# Views.py file for "Assignment 3" templates
# Create templates for the views created in your project and use them in the views.

from django.shortcuts import render

def home(request):
    # Your template for home logic here
    return render(request, 'home.html')

def room(request):
    # Your view2 logic here
    return render(request, 'room.html')

