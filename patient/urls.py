from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='pat-home'),
    path('pat-prof', views.ProfileView, name='patient-profile'),
    path('pat-app', views.AppointmentView, name='patient-appointment'),
    path('pat-upd-prof', views.updateProfileView, name='upd-prof'),
    path('pat-gen-inv', views.genInvoice, name='pat-gen-inv'),
    path('pat-inv', views.invoiceView, name='pat-inv'),
]