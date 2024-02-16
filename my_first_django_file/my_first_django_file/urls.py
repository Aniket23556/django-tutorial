"""
URL configuration for my_first_django_file project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# Assignment 1 Views in urls.py file
# In the project create at least 2 views for your project  in the urls.py file and make the project running.

# from django.contrib import admin
# from django.urls import path
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello World!")

# def room(request):
#     return HttpResponse("Room Page")


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', home, name='home'),
#     path('room/', room, name='room'),
# ]


# Assignment 2 Views in Views.py file and import view to urls file
# Modify your project by creating the same views in views.py file and make the necessary changes to run the project.

# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('akitir.urls')),
# ]


# Assignment 3 Templates
# Create templates for the views created in your project and use them in the views.

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('akitir.urls')),
]
