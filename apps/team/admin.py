from django.contrib import admin

# Register your models here.
from .models import Team, Invitation

admin.site.register(Team)
admin.site.register(Invitation)
