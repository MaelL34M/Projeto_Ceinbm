from principal.models import Diretor,ViceDiretor,Coordenador,Secretario,Funcionario,Docente,Discente,Disciplina,Turma,Turno,NotasDiscentes,PlanejamentoAnual,PlanoDeAula,PlanoDeCurso
from django import forms

class PlanejamentoAnualModelForm(forms.ModelForm):
    class Meta:
        model=PlanejamentoAnual
        fields='__all__'
        exclude=[
            'docente'
        ]
        widgets={
            'unidades_tematicas':forms.TextInput(attrs={'disabled':True})
        }