from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Project, Task
from apps.team.models import Team


@login_required
def projects(request):
    team = get_object_or_404(
        Team, pk=request.user.userprofile.active_team_id, status=Team.ACTIVE)
    projects = team.projects.all()

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            project = Project.objects.create(
                team=team, title=title, created_by=request.user)

            messages.info(request, 'Project added successfully!')

            return redirect('project:projects')

    return render(request, 'project/projects.html', {'team': team, 'projects': projects})


@login_required
def project(request, project_id):
    team = get_object_or_404(
        Team, pk=request.user.userprofile.active_team_id, status=Team.ACTIVE)
    project = get_object_or_404(Project, team=team, pk=project_id)

    if request.method == 'POST':
        title = request.GET.get('title')

        if title:
            task = Task.objects.create(team=team, project=project, title=title)
            messages.info(request, 'Task Added')

            # redirect the user back to product page
            return redirect('project:project', project_id=project_id)
    # get the tasks to show on project page
    tasks_todo = project.tasks.filter(status=Task.TODO)
    tasks_done = project.tasks.filter(status=Task.DONE)

    return render(request, 'project/project.html', {'team': team, 'project': project, 'tasks_todo': tasks_todo, 'tasks_done': tasks_done})


@login_required
def edit_project(request, project_id):
    team = get_object_or_404(
        Team, pk=request.user.userprofile.active_team_id, status=Team.ACTIVE)
    project = get_object_or_404(Project, team=team, pk=project_id)

    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            project.title = title
            project.save()

            messages.info(request, 'Your changes are saved')

            return redirect('project:project', project_id=project.id)

    return render(request, 'project/edit_project.html', {'team': team, 'project': project})
