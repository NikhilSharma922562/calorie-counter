from pyexpat import model
from django import forms
from ccapp.models import AppUser

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        #If we need all fields of model
        #fields = "__all__"

        #For login we only require email and password
        fields = ('email','password')

        model = AppUser

class RegistrationForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput)
     class Meta:
        fields = ('first_name','middel_name','last_name','email','contact','gender','dob',\
            'blood_group','password')

        model = AppUser
