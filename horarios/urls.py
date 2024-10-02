from django.urls import path
from .views import horario_list, horario_create, horario_update, horario_delete

urlpatterns = [
    path('list/', horario_list, name='horario_list'),
    path('create/', horario_create, name='horario_create'),
    path('<int:pk>/edit/', horario_update, name='horario_update'),
    path('<int:pk>/delete/', horario_delete, name='horario_delete'),
]