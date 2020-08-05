from django.urls import path, include

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'tea', views.MachinaView)

urlpatterns = [
    path(r'', include(router.urls)),
    path("machine/", views.TeaMachine.as_view()), #Add
    path("add/", views.AddGet.as_view()), #AddaGet
]
