# import django

from django.urls import path, include

from .views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('projects/', include('apps.project.urls')),
    path('myaccount/', include('apps.userprofile.urls')),
    path('myaccount/teams/', include('apps.team.urls')),
]
