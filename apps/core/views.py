# import functionality from Django
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# from .models import Userprofile
from apps.userprofile.models import Userprofile
from apps.team.models import Invitation

# Views


def frontpage(request):
    return render(request, 'core/frontpage.html')


def privacy(request):
    return render(request, 'core/privacy.html')


def terms(request):
    return render(request, 'core/terms.html')


def plans(request):
    return render(request, 'core/plans.html')

# views


def signup(request):
    userprofile = Userprofile.objects.create(user=request.user)
    # check if form is submitted
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # save user in db
            user = form.save()
            user.email = user.username
            user.save()

            # create user profile
            userprofile = Userprofile.objects.create(user=user)

            # Log in
            login(request, user)
            invitations = Invitation.objects.filter(
                email=user.email, status=Invitation.INVITED)

            if invitations:
                return redirect('team:accept_invitation')
            else:
                return redirect('dashboard')

    else:
        form = UserCreationForm()

        # form is available in the frontend
        # this form is for backend validation by Django
        return render(request, 'core/signup.html', {'form': form})
