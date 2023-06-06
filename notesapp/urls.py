from django.urls import path

from .views import note_list_view, note_detail_view, note_create_view, note_update_view

urlpatterns = [
    path('', note_list_view, name='note_list'),
    path('create/', note_create_view, name="note_create"),
    path('<int:pk>/', note_detail_view, name='note_detail'),
    path('<int:pk>/update/', note_update_view, name='note_update'),
]
