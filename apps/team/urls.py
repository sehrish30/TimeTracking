# import Django

# because our apps can have many add so we will create namespace

from django.urls import path

from .views import add, team, edit, activate_team, invite, plans

app_name = 'team'

urlpatterns = [
    path('add/', add, name="add"),
    path('<int:team_id>/', team, name="team"),
    path('invite/', invite, name="invite"),
    path('edit/', edit, name="edit"),
    path('plans/', plans, name="plans"),
    path('activate_team/<int:team_id>/', activate_team, name="activate_team"),
]
