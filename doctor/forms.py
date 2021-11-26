from django import forms
from .models import Prescription, DoctorProfile
from patient.models import PatientProfile

class PrescriptionCreationForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['symptoms', 'prescription', 'pat']
        def __init__(self, *args, **kwargs):
            model = Prescription
            user = kwargs.pop('user','')
            super(PrescriptionCreationForm, self).__init__(*args, **kwargs)
            self.fields['pat']=forms.ModelChoiceField(queryset=PatientProfile.objects.all())