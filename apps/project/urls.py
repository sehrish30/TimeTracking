# Import Django

from django.urls import path

from .views import projects, project

# Url pattern
app_name = 'project'
urlpatterns = [
    path('', projects, name="projects"),
    path('<int:project_id>/', project, name='project')
]
