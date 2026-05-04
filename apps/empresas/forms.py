from django import forms
from django.contrib.auth import get_user_model
from .models import Empresa

User = get_user_model()


class CadastroEmpresaUsuarioForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email',)
        widgets = {'email': forms.EmailInput(attrs={'class': 'form-control'})}

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('password1') != cleaned.get('password2'):
            self.add_error('password2', 'As senhas não coincidem.')
        return cleaned


class CadastroEmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('razao_social', 'nome_fantasia', 'cnpj', 'responsavel', 'telefone')
        widgets = {
            'razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_fantasia': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '00.000.000/0000-00'}),
            'responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }
