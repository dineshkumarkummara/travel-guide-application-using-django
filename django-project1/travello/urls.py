from django.urls import path
from . import views

urlpatterns = [
    path("travello",views.index,name='index'),
]
