from django.contrib import admin

# import project model and show in admin interface
#import models
from .models import Project

# Register your models here.
admin.site.register(Project)
