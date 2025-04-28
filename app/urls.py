from django.urls import path
from . import views
urlpatterns=[ 
    path("home_cars/",views.car1),
    path("car2/<int:id>",views.car2,name='kumar')
     ]