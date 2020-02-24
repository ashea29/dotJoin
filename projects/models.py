from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()



# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=100)
  startDate = models.DateField(max_length=100)
  endDate = models.DateField(max_length=100)

  def __str__(self):
    return self.title


class Task(models.Model):
  PROGRESS_CHOICES = (
    ('NS', 'Not Started'),
    ('ST', 'Started'),
    ('IP', 'In Progress'),
    ('AD', 'Almost Completed'),
    ('COMP', 'Completed')
  )

  project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
  title = models.CharField(max_length=100)
  startDate = models.DateField(max_length=100)
  duration = models.PositiveIntegerField(min_value=1)
  progress = models.CharField(max_length=4, choices=PROGRESS_CHOICES)
  teamMembers = models.ManyToManyField(User, through='TeamMember')

  def __str__(self):
    return self.title


class TeamMember(models.Model):
  task = models.ForeignKey(Task, related_name="teamMembers")
  user = models.ForeignKey(User, related_name="user_teams")

  def __str__(self):
    return self.user.username

  class Meta:
    unique_together = ("task", "user")