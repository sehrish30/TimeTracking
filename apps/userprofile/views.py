from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# import User model
from .models import Userprofile

# views
def signup(request):
    # check if form is submitted
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # save user in db
            user = form.save()
            user.email = user.username
            user.save()

            # create user profile
            userprofile = Userprofile.objects.create(user = user)

            # Log in
            login(request, user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()
        
        # form is available in the frontend
        # this form is for backend validation by Django
        return render(request, 'userprofile/signup.html', {'form': form})

@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')

