from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='courses_list'),  # Adiciona a URL para a lista de cursos
    path('create/', views.course_create, name='course_create'),
    path('edit/<int:course_id>/', views.course_edit, name='course_edit'),
    path('delete/<int:course_id>/', views.course_delete, name='course_delete'),
]