from django.shortcuts import render

# Create your views here.
# Import HttpResponse to send text-based responses
from django.http import HttpResponse

#----------------------------------------------------------------------------------------

# Define the home view function
def home(request):
    # Send a simple HTML response
    # This is the view function responding to your http resquest. 
    # HttpResponse object is the simplest way to return content in Django.
    # Home page - Send a simple html response
    # return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')
    # return render(request, '')
    # return render(request, 'templates')
    # return render(request, 'home.html') - Changed to index.html so that easier to find by Django program.
    return render(request, 'index.html')

    #GETTING ERROR MESSAGE ON PAGE FOR THIS -- SEE BELOW

    '''
IsADirectoryError at /
[Errno 21] Is a directory: '/Users/sylviaremington/code/ga/lectures/django-crud-app-cat-collector/main_app/templates'
Request Method:	GET
Request URL:	http://127.0.0.1:8000/
Django Version:	5.2.6
Exception Type:	IsADirectoryError
Exception Value:	
[Errno 21] Is a directory: '/Users/sylviaremington/code/ga/lectures/django-crud-app-cat-collector/main_app/templates'
Exception Location:	/Users/sylviaremington/.local/share/virtualenvs/django-crud-app-cat-collector-YF89FG1q/lib/python3.11/site-packages/django/template/loaders/filesystem.py, line 22, in get_contents
Raised during:	main_app.views.home
Python Executable:	/Users/sylviaremington/.local/share/virtualenvs/django-crud-app-cat-collector-YF89FG1q/bin/python3
Python Version:	3.11.13
Python Path:	
['/Users/sylviaremington/code/ga/lectures/django-crud-app-cat-collector',
 '/opt/homebrew/Cellar/python@3.11/3.11.13/Frameworks/Python.framework/Versions/3.11/lib/python311.zip',
 '/opt/homebrew/Cellar/python@3.11/3.11.13/Frameworks/Python.framework/Versions/3.11/lib/python3.11',
 '/opt/homebrew/Cellar/python@3.11/3.11.13/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload',
 '/Users/sylviaremington/.local/share/virtualenvs/django-crud-app-cat-collector-YF89FG1q/lib/python3.11/site-packages']
Server time:	Sun, 28 Sep 2025 18:21:49 +0000
    '''


#----------------------------------------------------------------------------------------

# Define an about view function
def about(request):
    # About page
    # return HttpResponse('<h1>About Me:</h1><h2>My name is Sylvia and I love to dance!</h2>')
    return render(request, 'about.html')

#----------------------------------------------------------------------------------------

#create a url for dresses page - done
#create a view for dresses page - done
#create a template for dresses page - done 
#return it as a render inside the view (dresses function) - done

#Define a dresses view function
def dresses(request):
    return render(request, 'dresses.html')

#----------------------------------------------------------------------------------------

#create url & function for cats page
#defining a cats view function
def cats(request):
    return render(request, 'cats.html')

#----------------------------------------------------------------------------------------

#defining cakes view function - creating function for cakes page
def cakes(request):
    return render(request, 'cakes.html')

#----------------------------------------------------------------------------------------

#defining cookies view function - creating function for cookies page
def cookies(request):
    return render(request, 'cookies.html')

#----------------------------------------------------------------------------------------