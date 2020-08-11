from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def hello_view(request):
    return render(request,'index.html',{'name':'dinesh'})
@csrf_exempt
def add(request):
    value1=int(request.POST['num1'])
    value2=int(request.POST['num2'])
    res=value1+value2
    return render(request,'result.html',{'result':res})
