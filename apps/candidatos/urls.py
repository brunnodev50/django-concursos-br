from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_candidato, name='cadastro_candidato'),
    path('perfil/', views.perfil_candidato, name='perfil_candidato'),
]
