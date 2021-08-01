
from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",create_flyer,name="create_flyer"),
    path("project_list",project_list,name="project_list"),

    # path('', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
 
  
]
