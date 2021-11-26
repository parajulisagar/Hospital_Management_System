from django.shortcuts import render, redirect
from .models import Prescription, DoctorProfile
from .forms import PrescriptionCreationForm
from reception.models import Appointments
from django.contrib.auth.decorators import login_required

@login_required
def homeView(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'D':
            return render(request, 'doctor/home.html')
        else:
            return redirect('login')

@login_required
def prescriptionView(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'D':
            obj = Prescription.objects.order_by('id').reverse()
            prescriptions = obj.filter(user=curr_user)
            total = obj.filter(user=curr_user).count()
            return render(request, 'doctor/prescription.html', {'prescriptions': prescriptions, 'total': total})
        else:
            return redirect('login')

@login_required
def createPrescription(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'D':
            if request.method == 'POST':
                form = PrescriptionCreationForm(request.POST)
                if form.is_valid():
                    form_obj = form.save(commit=False)
                    form_obj.user = curr_user
                    form_obj.save()
                    return redirect('doc-pres')
            
            else:
                form = PrescriptionCreationForm()
                return render(request, 'doctor/prescreate.html', {'form': form})
        else:
            return redirect('login')

@login_required
def appointmentView(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'D':
            doc = DoctorProfile.objects.get(user=curr_user)
            all_apps = Appointments.objects.all().filter(doc=doc, status='PD').order_by('time')
            return render(request, 'doctor/appointments.html', {'allapp': all_apps})
        else:
            return redirect('login')
