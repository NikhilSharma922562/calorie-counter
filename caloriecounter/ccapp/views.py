from email import contentmanager
from re import template
from tkinter.tix import Form
from django.shortcuts import render
from matplotlib.style import context

from ccapp.forms import LoginForm, RegistrationForm

# Create your views here.

def landing(request):
    template = 'index.html'
    context ={
        'page_content_title': 'Home Page', 
        'msg_welcome': 'welcome to calorie counter.',

    }
    return render(request, template, context)

#render()-use to render the templates/pages
#This function takes three parameter
#1. request - request from the client.
#2. template - html page direction.
#3. context - data that are passed to templates(must be of type dict) - is optional

def user_login(request):
    login_form = LoginForm()
    template ='users/login.html'

    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        context = {
            'form': login_form,
            'data': {
                    'email':email,
                    'password':password
            }
            }
        return render(request, template, context)
    else:
        context = {'form':LoginForm}
        return render(request, template, context)


def user_register(request):
    register_form = RegistrationForm()
    template ='users/create.html'
    context = {'form': register_form}
    return render(request, template, context)
    


def user_index(request):
    template = 'users/index.html'
    context ={
        'page_content_title': 'User Dashboard', 
        'page_content_body': 'welcome to calorie counter.',
    }
    return render(request, template, context)