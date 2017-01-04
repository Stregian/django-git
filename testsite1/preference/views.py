from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

def preferencehomepage(request):
    http = 'this page should have two choices on it. At some point.'
    return HttpResponse(http)
