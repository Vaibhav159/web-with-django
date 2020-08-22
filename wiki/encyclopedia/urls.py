from encyclopedia.views import randomPage, showPage
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.showPage, name="showPage"),
    path("random", views.randomPage, name="random"),
    path("search", views.searchTopic, name="search"),
    path("newPage", views.newPage, name="newPage"),
    path("wiki/<str:name>/edit", views.editPage, name="editPage")
]
