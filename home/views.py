from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from doctor.models import DoctorProfile
from patient.models import PatientProfile
from user.models import UserProfile
from django.contrib.auth.decorators import login_required

def homeView(request):
    return render(request, 'home/home.html', {'title': 'Home| Hospital'})

def registerView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            label = form.cleaned_data.get('label')
            user = UserProfile.objects.get(username=username)

            if label == 'P':
                pat_id = 'pat-'+user.first_name[0:3]+'-'+str(user.id)
                patient = PatientProfile(user=user, pat_id=pat_id)
                patient.save()
            if label == 'D':
                doctor = DoctorProfile(user=user)
                doctor.save()
            messages.success(request, 'Account created successfully for %s' %username)
            return redirect('login')
        else:
            messages.error(request, 'Sorry! This username is already taken. Try Logging in instead.')
            return redirect('register')
    else:
        form = RegistrationForm()
        return render(request, 'home/register.html', {'form': form, 'title': 'Register| Hospital'})

@login_required
def postloginView(request):
    if request.user.is_authenticated:
        curr_user = request.user
        label = curr_user.label

        if label == 'P':
            return redirect('pat-home')

        if label == 'D':
            return redirect('doc-home')

        if label == 'H':
            return redirect('hr-home')

        if label == 'R':
            return redirect('recp-home')