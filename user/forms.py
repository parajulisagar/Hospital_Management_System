from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UserProfile
        fields = ['username',]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ['username',]