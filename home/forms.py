from django import forms
from user.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=250, required=True)
    last_name = forms.CharField(label='Last Name', max_length=250, required=True)
    email = forms.EmailField(max_length=250)
    CHOICES=[('D', 'Doctor'),
         ('P','Patient'),
         ]
    label = forms.ChoiceField(choices=CHOICES, label='Register as')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError(u'Username "%s" is already in use.' % username)
        return username

    class Meta(UserCreationForm):
        model = UserProfile
        fields = ['first_name', 'last_name', 'username', 'email', 'label']