from django.contrib import admin

from webapp.models import Task, TaskType, TaskStatus, Project

admin.site.register(Task)
admin.site.register(TaskType)
admin.site.register(TaskStatus)
admin.site.register(Project)

