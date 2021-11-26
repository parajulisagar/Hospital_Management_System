from .models import PatientProfile
from user.models import UserProfile
from django import forms

class ProfileUpdateform(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['Phone', 'Gender', 'Age', 'Address', 'Blood_Group', 'Case_Paper_no', 'Profile_Picture']
        def __init__(self, *args, **kwargs):
            model = PatientProfile
            user = kwargs.pop('user','')
            super(ProfileUpdateform, self).__init__(*args, **kwargs)
            self.fields['user']=forms.ModelChoiceField(queryset=UserProfile.objects.all())