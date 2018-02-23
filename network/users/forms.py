from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from .models import Profile

import requests
# import clearbit

class SignUpForm(UserCreationForm):
    #first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    #last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def clean_email(self):
        """
            Inject ValidationError for emailhunter domain confirmation.
        """
        print (self.cleaned_data.get('email'))
        email = self.cleaned_data.get('email')
        #get data from emailhunter service
        url = f'https://api.hunter.io/v2/email-verifier?email={email}&api_key={settings.HUNTER_API_KEY}'
        response_json = requests.get(url).json()
        #smtp_check - True if domain exist
        if response_json['data']['smtp_check'] == False:
            raise forms.ValidationError("Domain doesn't exist, please, enter valid email!")
        return email

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'avatar']

    # def clean_bio(self):
    #     profile_user = User.objects.get(user=self.user)
    #     person = clearbit.Person.find(email=f'{profile_user.email}', stream=True)
    #     bio = self.cleaned_data.get('bio')
    #     if person != None:
    #         print ("Name: " + person['name']['fullName'])
    #         bio = person['aboutme']['bio']
    #     return bio
