from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Objects

# Create your views here.
def write(request):
   objects = Objects.objects.all()
   return render(request, 'index.html',{'object': objects})

def addwrite(request):
   objects = Objects.objects.all()
   newobject = request.POST('content')
   newobject.save()
   return render(request, 'index.html',{'objects': objects})
