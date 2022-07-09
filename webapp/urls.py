from django.urls import path
from django.views.generic import CreateView

from webapp.views import IndexView, TaskView, CreateTask, UpdateTask, DeleteTask

urlpatterns = [
    path('', IndexView.as_view(), name='IndexView'),
    path('task/<int:pk>', TaskView.as_view(), name='TaskView'),
    path('create/', CreateTask.as_view(), name='CreateTask'),
    path('product/<int:pk>/update/', UpdateTask.as_view(), name='UpdateTask'),
    path('product/<pk>/delete/', DeleteTask.as_view(), name='DeleteTask'),


]
