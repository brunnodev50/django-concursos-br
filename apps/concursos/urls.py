from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_concursos, name='lista_concursos'),
    path('<int:pk>/', views.detalhe_concurso, name='detalhe_concurso'),
    path('criar/', views.criar_concurso, name='criar_concurso'),
    path('<int:pk>/editar/', views.editar_concurso, name='editar_concurso'),
    path('<int:pk>/edital/', views.upload_edital, name='upload_edital'),
]
