from django.contrib import auth
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

TYPES = [('Task', 'задача'), ('Bug', 'ошибка'), ('Enhancement', 'улучшение')]
STATUSES = [('New', 'новый'), ('In Progress', 'в процессе'), ('Done', 'выполнено')]


# Create your models here.
class BaseModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_ad = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        abstract = True


class Task(BaseModel):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=2000, null=True, blank=True, )
    status = models.ForeignKey('webapp.TaskStatus', related_name='statuses', on_delete=models.CASCADE,
                               verbose_name='Статус')
    type = models.ManyToManyField('webapp.TaskType', related_name='types', blank=True)
    project = models.ForeignKey('webapp.Project', related_name='project', on_delete=models.CASCADE,
                                verbose_name='Проэкт')

    def __str__(self):
        return f'{self.title}'

    # def get_absolute_url(self):
    #     return reverse('TaskView', kwargs={'pk': self.pk})

    class Meta:
        db_table = "Task"
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class TaskType(models.Model):
    type = models.CharField(max_length=30, choices=TYPES)

    def __str__(self):
        return f'{self.type}'

    class Meta:
        db_table = "Types"
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class TaskStatus(models.Model):
    status = models.CharField(max_length=30, choices=STATUSES)

    def __str__(self):
        return f'{self.status}'

    class Meta:
        db_table = "Statuses"
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Project(models.Model):
    start = models.DateField(verbose_name='Дата начала')
    end = models.DateField(null=True, verbose_name='Дата окончания')
    title = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(max_length=2000, verbose_name='Описание')
    is_deleted = models.BooleanField(null=True,blank=True,default=False,verbose_name='Мягкое удаление')
    user = models.ManyToManyField('auth.User',verbose_name='Пользователь',related_name='projects')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('webapp:DetailProjectView', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Проэкт'
        verbose_name_plural = 'Проэкты'
