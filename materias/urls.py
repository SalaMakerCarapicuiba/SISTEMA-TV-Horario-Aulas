from django.urls import path
from .views import materia_list, materia_create, materia_update, materia_delete

urlpatterns = [
    path('list/', materia_list, name='materia_list'),
    path('create/', materia_create, name='materia_create'),
    path('<int:pk>/edit/', materia_update, name='materia_update'),
    path('<int:pk>/delete/', materia_delete, name='materia_delete'),
]