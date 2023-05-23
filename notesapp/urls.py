from django.urls import path

from .views import note_list_view

urlpatterns = [
    path('', note_list_view, name='note_list'),
]
