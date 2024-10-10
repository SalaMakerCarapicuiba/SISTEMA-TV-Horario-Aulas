from django.urls import path
from . import views


urlpatterns = [
    path('create/<int:course_id>/', views.turma_create, name='turma_create'),
    path('edit/<int:turma_id>/', views.turma_edit, name='turma_edit'),
    path('delete/<int:turma_id>/', views.turma_delete, name='turma_delete'),
]
