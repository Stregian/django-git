from django.shortcuts import render
from django.http import HttpResponse, Http404

from preference.models import Choice
from preference.forms import AddingForm
from preference.forms import TestForm
# Create your views here.

def preferencehomepage(request):
    #http = 'this page should have two choices on it. At some point.'
    #return HttpResponse(http)
    return render(request, 'main.html', {})
def add_choice(request):
    if request.method == 'POST':
        form = AddingForm(request.POST)
        if form.is_valid():
            option1 = form.cleaned_data['option1']
            option2 = form.cleaned_data['option2']
            number = form.cleaned_data['number']
            return HttpResponse('Thank you for submitting your choices')
            number = form.cleaned_data['number']
            C1 = Choice(text = option1)
            C1.save()
            C2 = Choice(text = option2)
            C2.save()
            return HttpResponse('Thank you for submitting your form, your second option was %s' %C2.text )
    else:
        form = AddingForm()
    return render(request,'addchoice.html',{'AddingForm':form})
    
def contact(request):
    http = 'a simple contact page'
    return HttpResponse(http)
