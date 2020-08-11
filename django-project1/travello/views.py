from django.shortcuts import render
from django.http import HttpResponse
from travello.models import Destination
# Create your views here.
def index(request):
    dest=Destination.objects.all()
    return render(request,"index.html",{'dests':dest})