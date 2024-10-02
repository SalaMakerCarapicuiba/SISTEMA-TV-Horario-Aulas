from django.urls import path
from .views import turma_list, turma_create, turma_update, turma_delete

urlpatterns = [
    path('list/', turma_list, name='turma_list'),
    path('create/', turma_create, name='turma_create'),
    path('<int:pk>/edit/', turma_update, name='turma_update'),
    path('<int:pk>/delete/', turma_delete, name='turma_delete'),
]