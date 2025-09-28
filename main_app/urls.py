from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # Routes will be added here
    # The urlpatterns list is where you specify each route and define it similar to 
    # how routes are defined/grouped in controllers in Express

    # FIRST ROUTE to display the homepage - HOMEPAGE ROUTE DEFINED HERE:
    path('', views.home, name='home'),
    # empty url, who's going to handle it, and a name for it
    #The default route is going to be "home" and there's going to be a function inside views called home
    # The above code defines a root path using an empty string and maps it to the view.home view function 
    # that does not exist yet - making the server unhappy. We’ll remedy this with a new view in the next step.
    # The name='home' kwarg is technically optional but will come in handy for referencing the URL 
    # in other parts of the app, especially from within templates, so we will always use it.

    #----------------------------------------------------------------------------------------

    # Create a route for ABOUT - create relevant function inside of views, 
    # and say something about yourself in that function returned as an http response
    # SET UP THE ROUTE HERE / CREATE A FUNCTION INSIDE OF VIEWS.PY / RETURN A HTTP RESPONSE
    path('about/', views.about, name='about'),






    



]
