from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userprofile(models.Model):
    user = models.ForeignKey(User, related_name='userprofile', on_delete=models.CASCADE)
    active_team_id = models.IntegerField(default = 0)
