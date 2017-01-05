from django import forms

class AddingForm(forms.Form):
    option1 = forms.CharField(widget=forms.Textarea, max_length = 300)
    option2 = forms.CharField(widget=forms.Textarea, max_length = 300)
    number = forms.IntegerField()

class TestForm(forms.Form):
    your_name = forms.CharField()
    
