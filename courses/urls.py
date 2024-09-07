from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_curso, name='cadastrar_curso'),
]