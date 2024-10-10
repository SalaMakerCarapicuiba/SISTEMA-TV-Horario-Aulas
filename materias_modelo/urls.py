from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:id>/', views.materia_modelo_create, name='materia_modelo_create'),
    path('edit/<int:id>/', views.materia_modelo_edit, name='materia_modelo_edit'),
    path('delete/<int:id>/', views.materia_modelo_delete, name='materia_modelo_delete'),
]