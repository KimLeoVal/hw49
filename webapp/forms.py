from pyexpat import model

from django import forms
from django.core import validators

from .CustomValidators import special_chars, special_words, check_count, check_status
from webapp.models import Task, TaskType, TaskStatus, Project


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=20, validators=(special_chars,))
    description = forms.CharField(max_length=2000, validators=(special_words,), widget=forms.Textarea)
    type = forms.ModelMultipleChoiceField(queryset=TaskType.objects.all(), widget=forms.CheckboxSelectMultiple,
                                          validators=(check_count,))
    status = forms.ModelChoiceField(queryset=TaskStatus.objects.all(), validators=(check_status,))

    class Meta:
        model = Task
        fields = ['title','description','type','status']

class TaskForm1(forms.ModelForm):
    title = forms.CharField(max_length=20, validators=(special_chars,))
    description = forms.CharField(max_length=2000, validators=(special_words,), widget=forms.Textarea)
    type = forms.ModelMultipleChoiceField(queryset=TaskType.objects.all(), widget=forms.CheckboxSelectMultiple,
                                          validators=(check_count,))
    status = forms.ModelChoiceField(queryset=TaskStatus.objects.all(), validators=(check_status,))

    class Meta:
        model = Task
        fields = '__all__'

class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Найти')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['is_deleted']


