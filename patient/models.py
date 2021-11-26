from django.db import models
from user.models import UserProfile
from hospital import settings

class PatientProfile(models.Model):
    Male = 'M'
    Female = 'F'
    Other = 'O'
    genderchoice = [
        (Male, 'Male'),
        (Female, 'Female'),
        (Other,'Other')
    ]
    A_plus = 'A+'
    A_minus = 'A-'
    B_plus = 'B+'
    B_minus = 'B-'
    bloodChoice = [
        (A_plus, 'A+ type'),
        (A_minus, 'A- Type'),
        (B_minus,'B- Type'),
        (B_plus, 'B+ Type')
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    phn = models.BigIntegerField(blank=True, null=True, name='Phone')
    pat_id = models.CharField(max_length=20, null=True, blank=True, unique=True)
    gender = models.CharField(max_length=1, choices=genderchoice, default='M', null=True, name='Gender')
    age = models.IntegerField(blank=True, null=True, name='Age')
    address = models.CharField(max_length=250, blank=True, null=True, name='Address')
    blood_group = models.CharField(max_length=2, choices=bloodChoice, null=True, name='Blood_Group')
    case_paper_no = models.IntegerField(null=True, name='Case_Paper_no')
    img = models.ImageField(null=True, blank=True, name='Profile_Picture')

    def __str__(self):
        return self.pat_id
