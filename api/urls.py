from django.urls import path

from . import views

urlpatterns = [
    path("tea/", views.HowToMakeTea.as_view()),
]