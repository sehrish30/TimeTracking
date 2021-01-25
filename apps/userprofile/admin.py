from django.contrib import admin

# Register your models here.
# Show userprofile in admin area
#import models
from .models import Userprofile


# register
admin.site.register(Userprofile)
