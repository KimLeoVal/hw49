from django.views.generic import ListView

from models import Project


class ProjectView(ListView):
    model = Project
    template_name = "for_project/indexProject.html"
    context_object_name = "projects"
