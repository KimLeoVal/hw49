from django.urls import path

from webapp.views import IndexView, TaskView, CreateTask, UpdateTask, DeleteTask, ProjectView, DetailProjectView, \
    CreateProject, CreateProjectTask, CreateTask1, UpdateProject, DeleteProject, SoftDeleteProject
app_name = 'webapp'
urlpatterns = [
    path('', IndexView.as_view(), name='IndexView'),
    path('task/<task_pk>', TaskView.as_view(), name='TaskView'),
    path('create/', CreateTask1.as_view(), name='CreateTask1'),
    path('product/<int:pk>/update/', UpdateTask.as_view(), name='UpdateTask'),
    path('product/<pk>/delete/', DeleteTask.as_view(), name='DeleteTask'),
    path('projects/', ProjectView.as_view(), name='ProjectView'),
    path('projects/<int:pk>', DetailProjectView.as_view(), name='DetailProjectView'),
    path('projects/create', CreateProject.as_view(), name='CreateProject'),
    path('projects/<int:pk>/task/add', CreateProjectTask.as_view(), name='CreateProjectTask'),
    path('projects/<int:pk>/update/', UpdateProject.as_view(), name='UpdateProject'),
    path('projects/<pk>/delete/', DeleteProject.as_view(), name='DeleteProject'),
    path('projects/<int:pk>/softdelete/', SoftDeleteProject.as_view(), name='SoftDeleteProject'),





]
