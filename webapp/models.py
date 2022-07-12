from django.db import models

TYPES = [('Task', 'задача'), ('Bug', 'ошибка'), ('Enhancement', 'улучшение')]
STATUSES = [('New', 'новый'), ('In Progress', 'в процессе'), ('Done', 'выполнено')]


# Create your models here.
class BaseModel(models.Model ):
    created_ad = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    updated_ad = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    class Meta:
        abstract =True

class Task(BaseModel):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=2000, null=True, blank=True, )
    status = models.ForeignKey('webapp.TaskStatus', related_name='statuses', on_delete=models.CASCADE,
                               verbose_name='Статус')
    type_old = models.ForeignKey('webapp.TaskType', related_name='types', on_delete=models.CASCADE,
                               verbose_name='Тип')
    def __str__(self):
        return f'{self.title}'


    class Meta:
        db_table="Task"
        verbose_name='Задача'
        verbose_name_plural='Задачи'

class TaskType(models.Model):
    type = models.CharField(max_length=30,choices=TYPES)

    def __str__(self):
        return f'{self.type}'

    class Meta:
        db_table = "Types"
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

class TaskStatus(models.Model):
    status = models.CharField(max_length=30,choices=STATUSES)

    def __str__(self):
        return f'{self.status}'

    class Meta:
        db_table = "Statuses"
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
