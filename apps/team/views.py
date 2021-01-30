# import python
from apps.team.utilities import send_invitation
import random
import stripe

# import django
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
from .models import Team, Invitation, Plan

# import helpers
from .utilities import send_invitation

# Views


# members_in means checking logged user is a member of team
@login_required
def team(request, team_id):
    team = get_object_or_404(
        Team, pk=team_id, status=Team.ACTIVE, members__in=[request.user])
    invitations = team.invitations.filter(status=Invitation.INVITED)
    return render(request, 'team/team.html', {'team': team, 'invitations': invitations})


@login_required
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            team = Team.objects.create(title=title, created_by=request.user)
            team.members.add(request.user)
            team.save()

           # in userProfile model I have active_team_id
            userprofile = request.user.userprofile
            userprofile.active_team_id = team.id
            userprofile.save()

            return redirect('myaccount')

    return render(request, 'team/add.html')


@login_required
def edit(request):
    team = get_object_or_404(Team, pk=request.user.userprofile.active_team_id,
                             status=Team.ACTIVE, members__in=[request.user])

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            team.title = title
            team.save()

            messages.info(request, 'The changes were saved')

            return redirect('team:team', team_id=team.id)

    return render(request, 'team/edit.html', {'team': team})


@login_required
def activate_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id,
                             status=Team.ACTIVE, members__in=[request.user])
    userprofile = request.user.userprofile
    userprofile.active_team_id = team.id
    userprofile.save()

    messages.info(request, 'The new team is activated ')
    return redirect('team:team', team_id=team.id)


@login_required
def invite(request):
    team = get_object_or_404(Team, pk=request.user.userprofile.active_team_id,
                             status=Team.ACTIVE)
    if request.method == 'POST':
        email = request.POST.get('email')

        # check this email hasnot been invited before
        if email:
            invitations = Invitation.objects.filter(team=team, email=email)

            if not invitations:
                # create four letter string
                code = ''.join(random.choice(
                    'abcdefghijklmnopqrstuvwxyz0123456789') for i in range(4))
                invitation = Invitation.objects.create(
                    team=team, email=email, code=code)

                messages.info(request, 'The user was invited')

                # user helper func to send invitation
                send_invitation(email, code, team)

                return redirect('team:team', team_id=team.id)
            else:
                messages.info(request, 'The user has already been invited')

    return render(request, 'team/invite.html', {'team': team})


@login_required
def plans(request):
    team = get_object_or_404(
        Team, pk=request.user.userprofile.active_team_id, status=Team.ACTIVE)
    error = ''

    if request.GET.get('cancel_plan', ''):
        try:
            plan_default = Plan.objects.get(is_default=True)

            team.plan = plan_default
            team.plan_status = Team.PLAN_CANCELLED
            team.save()

            # cancel subscription
            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe.Subscription.delete(team.stripe_subscription_id)
        except Exception:
            error = 'Something went wrong with the cancellation. Please try again!'

    context = {
        'team': team,
        'error': error,
        'stripe_pub_key': settings.STRIPE_PUBLISHABLE_KEY
    }

    return render(request, 'team/plans.html', context)
