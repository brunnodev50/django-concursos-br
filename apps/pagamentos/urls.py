from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:candidatura_pk>/', views.checkout, name='checkout_pagamento'),
    path('confirmacao/<int:pagamento_pk>/', views.confirmacao, name='confirmacao_pagamento'),
    path('webhook/mercadopago/', views.webhook_mercadopago, name='webhook_mercadopago'),
]
