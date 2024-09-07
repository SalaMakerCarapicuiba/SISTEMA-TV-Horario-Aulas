from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_professor, name='cadastrar_professor'),
]