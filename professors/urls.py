from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_professores, name="listar_professores"),
    path('cadastrar/', views.cadastrar_professor, name='cadastrar_professor'),
    path('deletar/<int:id>', views.deletar_professor, name='deletar_professor')
]