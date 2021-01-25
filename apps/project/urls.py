# Import Django

from django.urls import path

from .views import projects, project, edit_project

# Url pattern
app_name = 'project'
urlpatterns = [
    path('', projects, name="projects"),
    path('<int:project_id>/', project, name='project'),
    path('<int:project_id>/edit/', edit_project, name='edit_project')
]
