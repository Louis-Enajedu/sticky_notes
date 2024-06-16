from django.urls import path
from .views import note_list, note_detail, note_create, note_update, note_delete

urlpatterns = [
    path('', note_list, name='note_list'),
    path('note/<int:pk>/', note_detail, name='note_detail'),
    path('note/new/', note_create, name='note_create'),
    path('note/<int:pk>/edit/', note_update, name='note_update'),
    path('note/<int:pk>/delete/', note_delete, name='note_delete'),
]
