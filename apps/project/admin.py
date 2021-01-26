from django.contrib import admin

# import project model and show in admin interface
#import models
from .models import Project, Task, Entry

# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Entry)
