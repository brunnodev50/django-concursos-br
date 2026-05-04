from django import forms
from .models import Candidatura
from apps.concursos.models import Cargo


class CandidaturaForm(forms.ModelForm):
    class Meta:
        model = Candidatura
        fields = ('cargo',)
        widgets = {'cargo': forms.Select(attrs={'class': 'form-select'})}

    def __init__(self, concurso, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cargo'].queryset = Cargo.objects.filter(concurso=concurso)
        self.fields['cargo'].empty_label = 'Selecione o cargo'
