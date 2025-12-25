from django.urls import path
from access import views

# Create your urls here.

urlpatterns = [
    path(route='set-csrf', view=views.SetCSRFToken.as_view()), # /api/set-csrf
    path(route='check-user', view=views.CheckUser.as_view()), # /api/check-user
    path(route='login', view=views.AuthProcess.as_view()), # /api/login
    path(route='logout', view=views.AuthProcess.as_view()), # /api/logout
]