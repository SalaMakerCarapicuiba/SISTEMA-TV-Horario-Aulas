from django.urls import path
from django.urls import path
from .views import select_course_view, edit_course_view, cadastrar_curso

urlpatterns = [
    path('cadastrar/', cadastrar_curso, name='cadastrar_curso'),
    path('select/', select_course_view, name='select_course'),
    path('edit/<int:course_id>/', edit_course_view, name='edit_course'),
]