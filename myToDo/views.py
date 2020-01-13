from django.shortcuts import render
from .models import Data
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    data=Data.objects.all()
    return render(request,'myToDo/index.html',{'data':data})
def add(request):
    c=Data(text=request.POST.get('text'))
    c.save()
    return HttpResponseRedirect('/todo/')
def delete(request,id):
    c=Data.objects.get(id=id)
    c.delete()
    return HttpResponseRedirect('/todo/')