from django.urls import path
from .views import sala_list, sala_create, sala_update, sala_delete

urlpatterns = [
    path('list/', sala_list, name='sala_list'),
    path('create/', sala_create, name='sala_create'),
    path('<int:pk>/edit/', sala_update, name='sala_update'),
    path('<int:pk>/delete/', sala_delete, name='sala_delete'),
]