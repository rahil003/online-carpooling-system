from django import forms
from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm

class userform(ModelForm):
    username = forms.CharField(max_length=100,widget=forms.TextInput,)
    email = forms.CharField(max_length=100,widget=forms.TextInput)
    first_name = forms.CharField(max_length=100,widget=forms.TextInput)
    last_name = forms.CharField(max_length=100,widget=forms.TextInput)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)

    class Meta():
        model = User
        fields=['username','email','first_name','last_name','password']     
    

class RideForm(forms.ModelForm):  
    class Meta:  
        model = Ride  
        fields = ['name', 'source', 'destination','car','contact'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'source': forms.TextInput(attrs={ 'class': 'form-control' }),
            'destination': forms.TextInput(attrs={ 'class': 'form-control' }),
            'car': forms.TextInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),


      }