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
        return sum(entry.minutes for entry in self.entries.all())

    # get all tasks
    def num_tasks_todo(self):
        return self.tasks.filter(status=Task.TODO).count()


class Task(models.Model):

    # status choices
    TODO = 'todo'
    DONE = 'done'
    ARCHIVED = 'archived'

    CHOICES_STATUS = (
        (TODO, 'Todo'),
        (DONE, 'Done'),
        (ARCHIVED, 'Archived')
    )

    team = models.ForeignKey(Team, related_name='tasks',
                             on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        User, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=CHOICES_STATUS, default=TODO)

    # show recent ones
    class Meta:
        ordering = ['-created_at']

    # string representation
    def __str__(self):
        return self.title

    def registered_time(self):
        return sum(entry.minutes for entry in self.entries.all())


class Entry(models.Model):
    team = models.ForeignKey(Team, related_name='entries',
                             on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, related_name='entries', on_delete=models.CASCADE)
    task = models.ForeignKey(
        Task, related_name="entries", on_delete=models.CASCADE)
    minutes = models.IntegerField(default=0)
    is_tracked = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, related_name='entries', on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        if self.task:
            return f'{self.task.title} - {self.created_at}'

        return f'{self.created_at}'
