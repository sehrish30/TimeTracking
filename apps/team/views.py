from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Team
# Views


# members_in means checking logged user is a member of team
@login_required
def team(request, team_id):
    team = get_object_or_404(
        Team, pk=team_id, status=Team.ACTIVE, members__in=[request.user])
    return render(request, 'team/team.html', {'team': team})


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
