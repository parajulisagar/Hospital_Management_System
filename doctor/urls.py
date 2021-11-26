from django.urls import path 
from . import views

urlpatterns = [
    path('', views.homeView, name='doc-home'),
    path('pres', views.prescriptionView, name='doc-pres'),
    path('pres-create', views.createPrescription, name='create-pres'),
    path('doc-app', views.appointmentView, name='doc-apps'),
]