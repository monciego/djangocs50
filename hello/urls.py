from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("jericho", views.jericho, name="jericho"),
    path("mrRobot", views.mrRobot, name="mrRobot")
]