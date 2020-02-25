from django import forms
from .models import Project, Task, TeamMember


class ProjectForm(forms.ModelForm):

  class Meta:
    model = Project
    fields = ('title', 'startDate', 'endDate')



class TaskForm(forms.ModelForm):

  class Meta:
    model = Task
    fields = ('title', 'startDate', 'duration', 'progress', 'project',)


class TeamMemberForm(forms.ModelForm):

  class Meta:
    model = TeamMember
    fields = ('user', 'task')