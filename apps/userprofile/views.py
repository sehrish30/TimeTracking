from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# import User model
from .models import Userprofile
from apps.team.models import Team, Invitation
from apps.team.utilities import send_invitation_accepted


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


@login_required
def accept_invitation(request):
    if request.method == 'POST':

        # check if code is correct
        code = request.POST.get('code')

        invitations = Invitation.objects.filter(
            code=code, email=request.user.email)

        if invitations:
            invitation = invitations[0]
            invitation.status = Invitation.ACCEPTED
            invitation.save()

            # add this user as member to the team
            team = invitation.team
            team.members.add(request.user)
            team.save()

            userprofile = request.user.userprofile
            userprofile.active_team_id = team.id
            userprofile.save()

            messages.info(request, 'Invitation accepted')

            send_invitation_accepted(team, invitation)
            return redirect('team:team', team_id=team.id)
        else:
            messages.info(request, "Invitation was not found")

    else:
        return render(request, 'userprofile/accept_invitation.html')
