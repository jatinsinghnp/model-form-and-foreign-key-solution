from django.shortcuts import render

from app.models import Task
from .forms import TaskForm

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView


class HomePageView(TemplateView):
    template_name = "index.html"


class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = "task.html"
    success_url = "login_page"
    model = Task

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()

        return super(TaskCreateView, self).form_valid(form)


