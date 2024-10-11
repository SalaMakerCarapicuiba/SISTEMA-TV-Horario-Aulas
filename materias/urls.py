from django.urls import path
from .views import materia_list, materia_update, materia_delete

urlpatterns = [
    path('list/', materia_list, name='materia_list'),
    path('<int:turma_id>/<int:materia_id>/edit/', materia_update, name='materia_update'),
    path('<int:pk>/delete/', materia_delete, name='materia_delete'),
]