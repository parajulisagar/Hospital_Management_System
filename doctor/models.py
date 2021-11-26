from django.db import models
from patient.models import PatientProfile
from user.models import UserProfile

class DoctorProfile(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    phone = models.BigIntegerField(null=True)
    Male = 'M'
    Female = 'F'
    Other = 'O'
    genderchoice = [
        (Male, 'Male'),
        (Female, 'Female'),
        (Other,'Other')
    ]
    gender = models.CharField(max_length=1, choices=genderchoice, default='M', null=True)
    age = models.IntegerField(null=True)
    department = models.CharField(max_length=50, null=True)
    salary = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username

class Prescription(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    symptoms = models.CharField(max_length=2500, null=True)
    prescription = models.CharField(max_length=2500, null=True)
    pat = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.pat.pat_id

    

