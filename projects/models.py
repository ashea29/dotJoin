from django.db import models


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
  teamMember = models.ForeignKey('TeamMember', on_delete=models.CASCADE, related_name='tasks', blank=True)
  # teamMembers = models.ManyToManyField(User, through='TeamMember')

  def __str__(self):
    return self.title


class TeamMember(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="teamMembers")
  task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="teamMembers")

  def __str__(self):
    return self.user.username

  class Meta:
    unique_together = ("task", "user")