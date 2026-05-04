from django.urls import path
from .views import CustomLoginView, CustomLogoutView, SolicitarRedefinicaoSenhaView, RedefinirSenhaView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('redefinir-senha/solicitar/', SolicitarRedefinicaoSenhaView.as_view(), name='solicitar_redefinicao_senha'),
    path('redefinir-senha/<uuid:token>/', RedefinirSenhaView.as_view(), name='redefinir_senha'),
]
