from django.shortcuts import render
from django.http import HttpResponse, Http404

def sitehomepage(request):
    http = "this is the site homepage, there should be something here!"
    return HttpResponse(http)
