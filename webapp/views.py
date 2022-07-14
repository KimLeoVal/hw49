from django.db.models.functions import Lower
from django.http import QueryDict
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import TaskForm
from webapp.models import Task


class IndexView(TemplateView):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'index.html', {'tasks': tasks})



class TaskView(TemplateView):
    template_name = 'task.html'
    def get_context_data(self,  **kwargs):
        kwargs['task'] = get_object_or_404(Task, pk=kwargs['task_pk'])
        return super().get_context_data(**kwargs)


class CreateTask(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            type = form.cleaned_data.pop('type')
            new_task = form.save()
            new_task.type.set(type)
            return redirect("TaskView", task_pk=new_task.pk)
        return render(request, "create.html", {"form": form})

class UpdateTask(View):
    def get(self,request,*args,**kwargs):
        pk = kwargs['pk']
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(initial={
            "title": task.title,
            "description": task.description,
            "status": task.status,
            'type': task.type.all(),
        })
        return render(request, 'update.html', {'form': form})
    def post(self,request,*args,**kwargs):
        pk = kwargs['pk']
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(data=request.POST,instance=task)
        if form.is_valid():
            # task.title = form.cleaned_data.get("title")
            # task.description = form.cleaned_data.get("description")
            # task.status = form.cleaned_data.get("status")
            type = form.cleaned_data.pop('type')
            task = form.save()
            task.type.set(type)
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

