import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileUpdateform
from django.contrib.auth.decorators import login_required
from .models import PatientProfile
from reception.models import Appointments, Account

@login_required
def homeView(request):
    curr_user = request.user
    if curr_user.label == 'P':
        return render(request, 'patient/home.html')
    else:
        messages.error(request, 'Sorry! Your not a patient!')
        return redirect('login')
        

@login_required
def ProfileView(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'P':
            pat_prof = PatientProfile.objects.get(user=curr_user)
            return render(request, 'patient/profile.html', {'user_pat': pat_prof})
                
        else:
            messages.error(request, 'Sorry! Your not a patient!')
            return redirect('login')
    else:
        return redirect('login')

@login_required
def invoiceView(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'P':
            pat = PatientProfile.objects.get(user=curr_user)
            account = Account.objects.get(pat=pat)
            return render(request, 'patient/invoice.html', {'account': account})
        else:
            messages.error(request, 'Sorry! Your not a patient!')
            return redirect('login')
    else:
            return redirect('login')

@login_required
def genInvoice(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'P':
            buffer = io.BytesIO()
            p = canvas.Canvas(buffer)
            p.drawString(100, 100, "This is your invoice.")
            p.showPage()
            p.save()
            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename='invoice_hospital.pdf')
        else:
            messages.error(request, 'Sorry! Your not a patient!')
            return redirect('login')
    else:
            return redirect('login')

@login_required
def AppointmentView(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'P':
            pat = PatientProfile.objects.get(user=curr_user)
            all_apps = Appointments.objects.all().filter(pat=pat).order_by('time')
            return render(request, 'patient/appointments.html', {'allapp': all_apps})
        else:
            messages.error(request, 'Sorry! Your not a patient!')
            return redirect('login')
    else:
            return redirect('login')

@login_required
def updateProfileView(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'P':
            pat = PatientProfile.objects.get(user=curr_user)
            if request.method == 'POST':
                pat.Phone = request.POST.get('phn')
                pat.Gender = request.POST.get('gender')
                pat.Age = request.POST.get('age')
                pat.Address = request.POST.get('address')
                pat.Blood_Group = request.POST.get('bg')
                pat.save()
                return redirect('patient-profile')

            else:
                messages.error(request, 'Sorry! Your not a patient!')
                return render(request, 'patient/updProfile.html', {'pat': pat})

        else:
            return redirect('login')
    else:
            return redirect('login')
