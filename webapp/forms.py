from pyexpat import model


from django import forms
from django.forms import widgets

from webapp.models import Task, TaskType, TaskStatus


class TaskForm(forms.ModelForm):
    type = forms.ModelMultipleChoiceField(queryset=TaskType.objects.all())
    status = forms.ModelChoiceField(queryset=TaskStatus.objects.all())
    class Meta:
        model = Task
        fields = '__all__'






