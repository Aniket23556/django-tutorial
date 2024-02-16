# Url.py file in django app.


#Assignment2
# In the code below we have created a url pattern for our view1 and view2 functions.

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.view1, name='view1'),
#     path('view2/', views.view2, name='view2'),
# ]




#Assignment3
# In the code below we have created a url pattern for our home and room function templates
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/', views.room, name='room'),
]

