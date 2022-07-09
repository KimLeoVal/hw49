from django.db.models.functions import Lower
from django.http import QueryDict
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from webapp.forms import TaskForm
from webapp.models import Task


class IndexView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'index.html', {'tasks': tasks})


class TaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task.html', {'task': task})


#
#
class CreateTask(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            description = form.cleaned_data.get("description")
            status = form.cleaned_data.get("status")
            type = form.cleaned_data.get("type")
            new_task = Task.objects.create(title=title, description=description, status=status, type=type)
            return redirect("TaskView", pk=new_task.pk)
        return render(request, "create.html", {"form": form})

class UpdateTask(View):
    def get(self,request,*args,**kwargs):
        pk = kwargs['pk']
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(initial={
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "type": task.type,
        })
        return render(request, 'update.html', {'form': form})
    def post(self,request,*args,**kwargs):
        pk = kwargs['pk']
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data.get("title")
            task.description = form.cleaned_data.get("description")
            task.status = form.cleaned_data.get("status")
            task.type = form.cleaned_data.get("type")
            task.save()
            return redirect('IndexView')
        return render(request, 'update.html', {"form": form})


class DeleteTask(View):
    def get(self,request,*args,**kwargs):
        pk = kwargs['pk']
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'delete.html',{'task':task})
    def post(self,request,*args,**kwargs):
        pk = kwargs['pk']
        task = get_object_or_404(Task, pk=pk)
        if request.POST.get('Yes')=='Да':
            task.delete()
        return redirect('IndexView')
#

