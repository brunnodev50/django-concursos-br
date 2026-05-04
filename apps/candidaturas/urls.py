from django.urls import path
from . import views

urlpatterns = [
    path('concurso/<int:concurso_pk>/candidatar/', views.candidatar, name='candidatar'),
    path('minhas/', views.minhas_candidaturas, name='minhas_candidaturas'),
]
