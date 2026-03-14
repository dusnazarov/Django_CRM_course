
from . import views
from django.urls import path

urlpatterns = [    
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
   
]
