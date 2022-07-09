from pyexpat import model


from django import forms
from django.forms import widgets

from webapp.models import Task, TaskType


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'






