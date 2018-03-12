from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.db import transaction
from django.conf import settings

from .forms import SignUpForm, UserForm, ProfileForm
from posts.models import Post

import clearbit

# signup form
@transaction.atomic
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            """ Clearbit connection """
            user            = form.save(commit=False)
            # get json data
            clearbit.key    = settings.CLEARBIT_API_KEY
            person          = clearbit.Person.find(email=f'{user.email}', stream=True)
            # update user&profile fields with clearbit data and save it
            if person != None: # if api finds data on server side
                # get user data
                user.first_name = person['name']['givenName']
                user.last_name  = person['name']['familyName']
                user.save()

                #get profile data
                user.profile.bio        = person['aboutme']['bio']
                # they don't provide bio anymore for default alex@clearbit.com email
                user.profile.location   = person['location']
                user.profile.save()
            else:
                user.save()
            login(request, user)
            return redirect('homepage')
    else: #method GET
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

# profile edit view
@login_required(login_url="users:login")
@transaction.atomic
def profile_edit_view(request):
    if request.method == 'POST':
        # get/validate/save user&profile forms
        user_form       = UserForm(request.POST, instance=request.user)
        profile_form    = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('homepage')
        else:
            messages.error(request, _('Please correct the error below.'))
    else: # method GET
        user_form       = UserForm(instance=request.user)
        profile_form    = ProfileForm(instance=request.user.profile)
    return render(request, 'users/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form })

# profile view
@login_required(login_url="users:login")
def profile_view(request):
    user    = request.user
    posts   = Post.objects.filter(user=user)
    return render(request, 'users/profile.html', {
        'user':user,
        'posts':posts })

# profile view by user name
@login_required(login_url="users:login")
def profile_user_view(request, username):
    user    = User.objects.get(username=username)
    posts   = Post.objects.filter(user=user)
    return render(request, 'users/profile_user.html', {
        'user':user,
        'posts':posts })
