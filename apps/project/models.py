from django.db import models

# who created model for that project
from django.contrib.auth.models import User

# import models
from apps.team.models import Team

# Create your models here.


class Project(models.Model):
    team = models.ForeignKey(
        Team, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    created_by = models.ForeignKey(
        User, related_name='projects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # sort alphabatically
    class Meta:
        ordering = ['title']

   # string representation of this object
    def __str__(self):
        return self.title

    # get all the time on certain project
    def registered_time(self):
        return 0

    # get all tasks
    def num_tasks_todo(self):
        return 0  # self.tasks.filter(status = Task.TODO).count()
