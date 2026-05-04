from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'}),
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '••••••••'}),
    )


class SolicitacaoRedefinicaoSenhaForm(forms.Form):
    CANAL_CHOICES = [('email', 'E-mail'), ('whatsapp', 'WhatsApp')]
    email = forms.EmailField(
        label='E-mail cadastrado',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    canal = forms.ChoiceField(
        label='Receber link via',
        choices=CANAL_CHOICES,
        widget=forms.RadioSelect,
    )


class RedefinirSenhaForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='Nova senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label='Confirmar nova senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
