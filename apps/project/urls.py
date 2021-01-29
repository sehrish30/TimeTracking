# Import Django

from django.urls import path

from .api import api_start_timer, api_stop_timer, api_discard_timer
from .views import projects, project, edit_project, task, edit_task, edit_entry, delete_entry

# Url pattern
app_name = 'project'
urlpatterns = [
    path('', projects, name="projects"),
    path('<int:project_id>/', project, name='project'),
    path('<int:project_id>/edit/', edit_project, name='edit_project'),
    path('<int:project_id>/<int:task_id>/', task, name="task"),
    path('<int:project_id>/<int:task_id>/<int:entry_id>/edit/',
         edit_entry, name="edit_entry"),
    path('<int:project_id>/<int:task_id>/<int:entry_id>/delete/',
         delete_entry, name="delete_entry"),
    path('<int:project_id>/<int:task_id>/edit/', edit_task, name="edit_task"),

    # API
    path('api/start_timer/', api_start_timer, name="api_start_timer"),
    path("api/stop_timer/", api_stop_timer, name="api_stop_timer"),
    path("api/discard_timer/", api_discard_timer, name="api_discard_timer")

]
