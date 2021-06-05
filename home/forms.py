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