from django.contrib import admin

# Register your models here.
from .models import Team, Invitation, Plan

admin.site.register(Team)
admin.site.register(Invitation)
admin.site.register(Plan)
