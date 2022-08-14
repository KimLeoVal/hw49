from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator, Page
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import TaskForm, SearchForm, ProjectForm, TaskForm1, UserForm, ProjectFormUser
from webapp.models import Task, Project


class IndexView(ListView):
    model = Task
    template_name = "for_task/index.html"
    context_object_name = "tasks"
    ordering = "-updated_at"
    paginate_by = 6

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


class CreateTask(LoginRequiredMixin,CreateView):
    template_name = 'for_task/create.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('webapp:TaskView', kwargs={'pk': self.object.pk})

class CreateTask1(LoginRequiredMixin,CreateView):
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


class UpdateTask(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    context_object_name = 'task'
    template_name = 'for_task/update.html'


    def get_success_url(self):
        return reverse('webapp:TaskView',kwargs={'task_pk':self.object.pk})
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


class DeleteTask(LoginRequiredMixin,DeleteView):
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
    paginate_by = 10

    def get_queryset(self):
        return Project.objects.filter(is_deleted=False)


class DetailProjectView(DetailView):
    template_name = 'for_project/project.html'
    model = Project

    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        project = get_object_or_404(Project, pk=pk)
        if not project.is_deleted:
            context = {'project': project}
            return self.render_to_response(context)
        else:
            return HttpResponseNotFound('Project Not Found')





class CreateProject(PermissionRequiredMixin,CreateView):
    template_name = 'for_project/create.html'
    model = Project
    form_class = ProjectFormUser
    permission_required = 'webapp.add_project'



    def form_valid(self, form):
        project = form.save()
        user_id = self.request.user
        project.user.add(user_id)
        project.save()
        return super().form_valid(form)

        # project = form.save()
        # user_id = self.request.user
        # print(user_id)
        # print(project)
        # project.user.add(user_id,1)
        # print(project.user)
        # project.save()
        # print(project.user)
        # return redirect('webapp:DetailProjectView',pk= project.pk)





    # def get_success_url(self):
    #     return reverse('DetailProjectView', kwargs={'pk': self.object.pk})
class CreateProjectTask(PermissionRequiredMixin,CreateView):
    template_name = 'for_task/CreateTaskforProject.html'
    form_class = TaskForm

    def has_permission(self):
        """
        Override this method to customize the way permissions are checked.
        """
        perms = self.get_permission_required() or self.get_object().user == self.request.user
        return self.request.user.has_perms(perms)


    def form_valid(self, form):
        project = get_object_or_404(Project, pk = self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:DetailProjectView',kwargs={'pk':self.object.project.pk})

class UpdateProject(LoginRequiredMixin,UpdateView):
    model = Project
    template_name = 'for_project/update.html'
    form_class = ProjectForm
    context_object_name = 'project'

class DeleteProject(LoginRequiredMixin,DeleteView):
    model = Project
    context_object_name = 'project'
    template_name = 'for_project/delete.html'
    success_url = reverse_lazy('webapp:ProjectView')

class SoftDeleteProject(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        project.is_deleted = True
        project.save()
        return redirect('webapp:ProjectView')

class AddUserInProject(LoginRequiredMixin,UpdateView):
    model = Project
    template_name = 'for_project/adddeluser.html'
    form_class = UserForm
    context_object_name = 'project'

    def form_valid(self, form):
        # pk = self.kwargs.get('pk')
        # project= get_object_or_404(Project,pk = pk)
        project = form.save()
        user_id = self.request.POST.get('user')
        author=self.request.user.pk
        project.user.add(user_id,author)
        project.save()
        return redirect('webapp:DetailProjectView', pk=project.pk)


#






