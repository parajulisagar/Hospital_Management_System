from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='recp-home'),
    path('dash', views.dashboardView, name='recp-dash'),
    path('add-app', views.addAppointmentView, name='add-app'),
    path('upd-app', views.updateAppointmentView, name='upd-app'),
    path('upd-app-form/<int:pk>/', views.updateAppointmentFormView, name='upd-app-form'),
    path('del-app', views.deleteAppointmentView, name='del-app'),
    path('add-acc', views.addAccountInfo, name='add-acc'),
    path('upd-acc', views.updateAccountView, name='upd-acc'),
    path('upd-acc-form/<int:pk>/', views.updateAccountFormView, name='upd-acc-form'),
    path('del-acc', views.deleteAccountView, name='del-acc'),
]