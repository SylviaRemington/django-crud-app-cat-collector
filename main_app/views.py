from django.shortcuts import render

# Create your views here.
# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    # This is the view function responding to your http resquest. 
    # HttpResponse object is the simplest way to return content in Django.
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

# Define an about view function
def about(request):
    return HttpResponse('<h2>About Me: My name is Sylvia and I love to dance!</h2>')



