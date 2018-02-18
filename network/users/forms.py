from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=50, label='Your name')
    email = forms.EmailField(max_length=254, required=True,
        error_messages={'required': 'Please enter your name'}, label='Your email')

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'avatar']
