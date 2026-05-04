from django import forms
from .models import Concurso, Cargo, Edital, ESTADOS_BR


class ConcursoForm(forms.ModelForm):
    class Meta:
        model = Concurso
        fields = (
            'titulo', 'descricao', 'orgao', 'estado', 'cidade',
            'vagas_total', 'taxa_inscricao', 'data_abertura', 'data_fechamento',
            'data_prova', 'status',
        )
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'orgao': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'vagas_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'taxa_inscricao': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'data_abertura': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_fechamento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_prova': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ('nome', 'nivel_escolaridade', 'salario', 'vagas', 'vagas_pcd')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel_escolaridade': forms.TextInput(attrs={'class': 'form-control'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'vagas': forms.NumberInput(attrs={'class': 'form-control'}),
            'vagas_pcd': forms.NumberInput(attrs={'class': 'form-control'}),
        }


CargoFormSet = forms.inlineformset_factory(
    Concurso, Cargo, form=CargoForm, extra=1, can_delete=True,
)


class EditalForm(forms.ModelForm):
    class Meta:
        model = Edital
        fields = ('titulo', 'arquivo', 'retificacao')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'retificacao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class FiltroConcursoForm(forms.Form):
    q = forms.CharField(
        required=False,
        label='Buscar',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cargo, órgão...'}),
    )
    estado = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos os estados')] + ESTADOS_BR,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    cidade = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
    )
