from django.shortcuts import render
from django.http import HttpResponse, Http404

def sitehomepage(request):
    return render(request,'home.html',{})
