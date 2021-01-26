# import django

from django.urls import path, include

urlpatterns = [
    path('projects/', include('apps.project.urls')),
    path('myaccount/', include('apps.userprofile.urls')),
    path('myaccount/teams/', include('apps.team.urls')),
]
