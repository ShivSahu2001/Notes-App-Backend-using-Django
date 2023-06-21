from django.urls import path
from . import views

urlpatterns = [
    # name parameter allows to access the routes dynamically
    path("", views.getRoutes, name="routes"),
    path("notes/", views.getNotes, name="notes"),
    # path("notes/create/", views.createNote, name="create-note"),
    # path("notes/<str:pk>/", views.getNoteById, name="note")
    # path("notes/update/<pk>/", views.updateNote, name="update-note"),
    # path("notes/delete/<pk>/", views.deleteNotes, name="delete-note"),
    path("notes/<pk>/", views.getNoteById, name="note")
]
