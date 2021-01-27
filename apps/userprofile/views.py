from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# import User model
from .models import Userprofile
from apps.team.models import Team


@login_required
def myaccount(request):
    teams = request.user.teams.exclude(
        pk=request.user.userprofile.active_team_id)
    return render(request, 'userprofile/myaccount.html', {'teams': teams})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()

        messages.info(request, 'Your changes are saved')

        return redirect('myaccount')

    return render(request, 'userprofile/edit_profile.html')
