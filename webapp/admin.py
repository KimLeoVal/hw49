from django.contrib import admin

from webapp.models import Task, TaskType, TaskStatus

admin.site.register(Task)
admin.site.register(TaskType)
admin.site.register(TaskStatus)
