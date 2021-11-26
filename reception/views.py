from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointments, Account
from .forms import AddAppointmentForm, addAccountInfoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

@login_required
def homeView(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'R':
            return render(request, 'reception/home.html')
        else:
            return redirect('login')

@login_required
def dashboardView(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'R':
            total = Appointments.objects.all().count()
            completed = Appointments.objects.filter(status = 'CT').count()
            pending = total-completed
            allapps = Appointments.objects.all()
            allacc = Account.objects.all()
            return render(request, 'reception/dashboard.html', 
            {'total':total, 'completed': completed, 'pending': pending, 'allapps': allapps, 'allacc': allacc})
        else:
            return redirect('login')

@login_required
def addAppointmentView(request, pk=0):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'R':
            if request.method == 'POST':
                form = AddAppointmentForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('recp-dash')
                else:
                    messages.error(request, 'Sorry! Something went wrong!')
                    return redirect('recp-home')
            else:
                form = AddAppointmentForm()
                return render(request, 'reception/addApp.html', {'form': form})
        else:
            return redirect('login')


@login_required
@csrf_exempt
def updateAppointmentView(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'R':
            if request.method == 'POST':
                app_id = request.POST.get('pk')
                return redirect(reverse('upd-app-form', args=(app_id,)))

@login_required
def updateAppointmentFormView(request, pk=0):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'R':
            app_id = pk
            appointment = Appointments.objects.get(pk=app_id)
            if request.method == 'POST':
                status = request.POST.get('status')
                appointment.status = status
                appointment.save()
                return redirect('recp-dash')
            else:
                return render(request, 'reception/updApp.html', {'appointment': appointment})

@login_required
@csrf_exempt
def deleteAppointmentView(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'R':
            if request.method == 'POST':
                app_id = request.POST.get('pk')
                appointment = Appointments.objects.get(pk=app_id)
                appointment.delete()
                return redirect('recp-dash')

@login_required
def addAccountInfo(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'R':
            if request.method == 'POST':
                form = addAccountInfoForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('recp-dash')
                else:
                    messages.error(request, 'Sorry! Something went wrong!')
                    return redirect('recp-home')
            else:
                form = addAccountInfoForm()
                return render(request, 'reception/addApp.html', {'form': form})
        else:
            return redirect('login')

@login_required
@csrf_exempt
def updateAccountView(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'R':
            if request.method == 'POST':
                acc_id = request.POST.get('pk')
                return redirect(reverse('upd-acc-form', args=(acc_id,)))

@login_required
def updateAccountFormView(request, pk=0):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'R':
            app_id = pk
            account = Account.objects.get(pk=app_id)
            if request.method == 'POST':
                paid = request.POST.get('paid')
                total = request.POST.get('total')
                account.paid = paid
                account.total = total
                account.save()
                return redirect('recp-dash')
            else:
                return render(request, 'reception/updAcc.html', {'account': account})

@login_required
@csrf_exempt
def deleteAccountView(request):
    if request.user.is_authenticated:
        curr_user = request.user
        if curr_user.label == 'R':
            if request.method == 'POST':
                app_id = request.POST.get('pk')
                account = Account.objects.get(pk=app_id)
                account.delete()
                return redirect('recp-dash')