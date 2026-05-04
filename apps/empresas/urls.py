from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro_empresa, name='cadastro_empresa'),
    path('dashboard/', views.dashboard_empresa, name='dashboard_empresa'),
]
