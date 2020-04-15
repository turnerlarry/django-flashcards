from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add.html', views.add, name="add"),
    path('subtract.html', views.subtract, name="subtract"),
    path('multiply.html', views.multiply, name="multiply"),
   
]
