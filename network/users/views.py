from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.db import transaction
from django.conf import settings
from .forms import SignUpForm, UserForm, ProfileForm
import clearbit
# Create your views here.
@transaction.atomic
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            """
             Clearbit connection
            """
            user = form.save(commit=False)
            # profile_user = User.objects.get(user=self.user)
            clearbit.key = settings.CLEARBIT_API_KEY
            person = clearbit.Person.find(email=f'{user.email}', stream=True)
            #     bio = self.cleaned_data.get('bio')
            if person != None:
                print ("Name: " + person['name']['fullName'])
                user.first_name = person['name']['givenName']
                user.last_name = person['name']['familyName']
                user.save()
                user.profile.bio = person['aboutme']['bio']
                user.profile.location = person['location']

                user.profile.save()
            #     return bio
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

@login_required(login_url="/users/login/")
@transaction.atomic
def profile_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid() and user_form.is_valid():
            # user_form.save()
            profile_form.save()
            # print(user_form.email + 'inside if')
            user_form.save()
            # messages.success(request, _('Your profile was successfully updated!'))
            return redirect('homepage')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        # print(user_form.email + 'inside else')
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
