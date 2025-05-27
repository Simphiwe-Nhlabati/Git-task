from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_sticky_notes, name='read_sticky_notes'),
    path('notes/templates/', views.create_sticky_notes, name='create_sticky_notes'),
    path('notes/<int:pk>/Update/', views.update_sticky_notes, name='update_sticky_notes'),
    path('notes/<int:pk>/Delete/', views.delete_sticky_notes, name='delete_sticky_notes'),
]


