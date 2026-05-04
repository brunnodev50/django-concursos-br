from django import forms
from django.contrib.auth import get_user_model
from django.db import transaction

from .models import Candidato, Telefone

User = get_user_model()


class CadastroUsuarioForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label='Confirmar senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ('email',)
        widgets = {'email': forms.EmailInput(attrs={'class': 'form-control'})}

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password1')
        p2 = cleaned.get('password2')
        if p1 and p2 and p1 != p2:
            self.add_error('password2', 'As senhas não coincidem.')
        return cleaned


class CadastroCandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = (
            'foto', 'nome_completo', 'cpf', 'rg', 'orgao_emissor',
            'nome_mae', 'nome_pai', 'renda_mensal', 'data_nascimento',
        )
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'orgao_emissor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SSP/SP'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_pai': forms.TextInput(attrs={'class': 'form-control'}),
            'renda_mensal': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
        }


class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = ('numero', 'tipo', 'tem_whatsapp')
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(11) 99999-9999'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'tem_whatsapp': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


TelefoneFormSet = forms.inlineformset_factory(
    Candidato,
    Telefone,
    form=TelefoneForm,
    extra=2,
    max_num=2,
    min_num=1,
    validate_min=True,
    can_delete=False,
)
