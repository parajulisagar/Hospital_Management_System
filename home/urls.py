from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('register/', views.registerView, name='register'),
    path('postlog/', views.postloginView, name='post-login'),
]