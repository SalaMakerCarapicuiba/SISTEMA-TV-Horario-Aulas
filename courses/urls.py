from django.urls import path
from .views import select_course_view, edit_course_view, cadastrar_curso, delete_course, course_list

urlpatterns = [
    path('cadastrar/', cadastrar_curso, name='cadastrar_curso'),
    path('select/', select_course_view, name='select_course'),
    path('edit/<int:course_id>/', edit_course_view, name='edit_course'),
    path('delete_course/<int:course_id>/', delete_course, name='delete_course'),
    path('courses/', course_list, name='course_list'),  # Adiciona a URL para a lista de cursos
]