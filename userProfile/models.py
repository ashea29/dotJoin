from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from projects.models import Project


# Create your models here.
class Profile(models.Model):
  user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
  projects = models.ForeignKey(Project, related_name='projects', on_delete=models.CASCADE)