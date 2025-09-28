from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # Routes will be added here
    # The urlpatterns list is where you specify each route and define it similar to 
    # how routes are defined/grouped in controllers in Express

    # First route to display the homepage - HOMEPAGE ROUTE DEFINED HERE:
    path('', views.home, name='home'),
    # The above code defines a root path using an empty string and maps it to the view.home view function 
    # that does not exist yet - making the server unhappy. We’ll remedy this with a new view in the next step.
    # The name='home' kwarg is technically optional but will come in handy for referencing the URL 
    # in other parts of the app, especially from within templates, so we will always use it.
    
]
