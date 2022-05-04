from turtle import home
from django.urls import path
from django.contrib.auth.views import LoginView

from .views import HomePageView, TaskCreateView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("task/", TaskCreateView.as_view(), name="task_create"),
    path(
        "login/",
        LoginView.as_view(
            template_name="authentication/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
]
