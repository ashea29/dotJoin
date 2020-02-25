from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()



# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=100)
  startDate = models.DateField(max_length=25)
  endDate = models.DateField(max_length=25)

  def __str__(self):
    return self.title


class Task(models.Model):
  PROGRESS_CHOICES = (
    ('NS', 'Not Started'),
    ('ST', 'Started'),
    ('IP', 'In Progress'),
    ('AC', 'Almost Completed'),
    ('CM', 'Completed')
  )

  project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
  title = models.CharField(max_length=100)
  startDate = models.DateField(max_length=25)
  dueDate = models.DateField(max_length=25)
  progress = models.CharField(max_length=2, choices=PROGRESS_CHOICES)
  # teamMembers = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name='tasks')
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