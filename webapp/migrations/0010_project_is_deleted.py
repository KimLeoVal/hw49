# Generated by Django 4.0.5 on 2022-07-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_alter_project_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_deleted',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Мягкое удаление'),
        ),
    ]
