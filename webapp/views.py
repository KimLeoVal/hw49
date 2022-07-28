from django.core.paginator import Paginator, Page
from django.db.models import Q

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import TaskForm, SearchForm, ProjectForm, TaskForm1
from webapp.models import Task, Project


class IndexView(ListView):
    model = Task
    template_name = "for_task/index.html"
    context_object_name = "tasks"
    ordering = "-updated_at"
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.search_value:
            return Task.objects.filter(
                Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return Task.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["form"] = self.form
        if self.search_value:
            query = urlencode({'search': self.search_value})
            context['query'] = query
            context['search'] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get("search")


class TaskView(TemplateView):
    template_name = 'for_task/task.html'

    def get_context_data(self, **kwargs):
        kwargs['task'] = get_object_or_404(Task, pk=kwargs['task_pk'])
        return super().get_context_data(**kwargs)


class CreateTask(CreateView):
    template_name = 'for_task/create.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('TaskView', kwargs={'pk': self.object.pk})

class CreateTask1(CreateView):
    template_name = 'for_task/create.html'
    form_class = TaskForm1

    def get_success_url(self):
        return reverse('TaskView', kwargs={'task_pk': self.object.pk})
    # def get(self, request, *args, **kwargs):
    #     form = TaskForm()
    #     return render(request, 'for_task/create.html', {'form': form})
    #
    # def post(self, request, *args, **kwargs):
    #     form = TaskForm(data=request.POST)
    #     if form.is_valid():
    #         type = form.cleaned_data.pop('type')
    #         new_task = form.save()
    #         new_task.type.set(type)
    #         return redirect("TaskView", task_pk=new_task.pk)
    #     return render(request, "for_task/create.html", {"form": form})


class UpdateTask(UpdateView):
    model = Task
    form_class = TaskForm
    context_object_name = 'task'
    template_name = 'for_task/update.html'


    def get_success_url(self):
        return reverse('TaskView',kwargs={'task_pk':self.object.pk})
    # def get(self, request, *args, **kwargs):
    #     pk = kwargs['pk']
    #     task = get_object_or_404(Task, pk=pk)
    #     form = TaskForm(initial={
    #         "title": task.title,
    #         "description": task.description,
    #         "status": task.status,
    #         'type': task.type.all(),
    #     })
    #     return render(request, 'for_task/update.html', {'form': form})
    #
    # def post(self, request, *args, **kwargs):
    #     pk = kwargs['pk']
    #     task = get_object_or_404(Task, pk=pk)
    #     form = TaskForm(data=request.POST, instance=task)
    #     if form.is_valid():
    #         type = form.cleaned_data.pop('type')
    #         task = form.save()
    #         task.type.set(type)
    #         return redirect('IndexView')
    #     return render(request, 'for_task/update.html', {"form": form})


class DeleteTask(DeleteView):
    model = Task
    template_name = 'for_task/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('IndexView')
    # def get(self, request, *args, **kwargs):
    #     pk = kwargs['pk']
    #     task = get_object_or_404(Task, pk=pk)
    #     return render(request, 'for_task/delete.html', {'task': task})
    #
    # def post(self, request, *args, **kwargs):
    #     pk = kwargs['pk']
    #     task = get_object_or_404(Task, pk=pk)
    #     if request.POST.get('Yes') == 'Да':
    #         task.delete()
    #     return redirect('IndexView')

class ProjectView(ListView):
    model = Project
    template_name = "for_project/indexProject.html"
    context_object_name = "projects"
    paginate_by = 2


class DetailProjectView(DetailView):
    template_name = 'for_project/project.html'
    model = Project



class CreateProject(CreateView):
    template_name = 'for_project/create.html'
    model = Project
    form_class = ProjectForm

    # def get_success_url(self):
    #     return reverse('DetailProjectView', kwargs={'pk': self.object.pk})
class CreateProjectTask(CreateView):
    template_name = 'for_task/CreateTaskforProject.html'
    form_class = TaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk = self.kwargs.get('pk'))
        print(project)
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('DetailProjectView',kwargs={'pk':self.object.project.pk})

class UpdateProject(UpdateView):
    model = Project
    template_name = 'for_project/update.html'
    form_class = ProjectForm
    context_object_name = 'project'