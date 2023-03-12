from principal.models import Diretor,ViceDiretor,Coordenador,Secretario,Funcionario,Docente,Discente,Disciplina,Turma,Turno,NotasDiscentes,PlanejamentoAnual,PlanoDeAula,PlanoDeCurso
from django import forms


class DiretorModelForm(forms.ModelForm):
    class Meta:
        model=Diretor
        fields='__all__'
        exclude=[
            'user',
            'cargo'
        ]
        widgets={
            'senha': forms.PasswordInput
        }
class ViceDiretorModelForm(forms.ModelForm):
    class Meta:
        model=ViceDiretor
        fields='__all__'
        exclude=[
            'user',
            'cargo'
        ]
        widgets={
            'senha': forms.PasswordInput
        }  
class CoordenadorModelForm(forms.ModelForm):
    class Meta:
        model=Coordenador
        fields='__all__'
        exclude=[
            'user',
            'cargo'
        ]
        widgets={
            'senha': forms.PasswordInput
        }
class SecretarioModelForm(forms.ModelForm):
    class Meta:
        model=Secretario
        fields='__all__'
        exclude=[
            'user',
            'cargo'
        ]
        widgets={
            'senha': forms.PasswordInput
        }
class FuncionarioModelForm(forms.ModelForm):
    class Meta:
        model=Funcionario
        fields='__all__'
        exclude=[
            'user'
        ]
        widgets={
            'senha': forms.PasswordInput
        }
class DisciplinaModelForm(forms.ModelForm):
    class Meta:
        model=Disciplina
        fields='__all__'
class DocenteModelForm(forms.ModelForm):
    class Meta:
        model=Docente
        fields='__all__'
        exclude=[
            'user',
            'cargo',
            'documentos'
        ]
        widgets={
            'senha': forms.PasswordInput,
            'disciplinas':forms.CheckboxSelectMultiple
        }
class DiscenteModelForm(forms.ModelForm):
    class Meta:
        model=Discente
        fields='__all__'
        exclude=[
            'user',
            'cargo',
            'disciplinas'
        ]
        widgets={
            'senha': forms.PasswordInput,
            'disciplinas': forms.CheckboxSelectMultiple()
        }
class TurmaModelForm(forms.ModelForm):
    class Meta:
        model=Turma
        fields='__all__'

class TurnoModelForm(forms.ModelForm):
    class Meta:
        model=Turno
        fields='__all__'
    
class NotasDiscentesModelForm(forms.ModelForm):
    class Meta:
        model=NotasDiscentes
        fields='__all__'
        exclude=[
            'disciplina',
            'discente',
            'media'
        ]
class PlanejamentoAnualModelForm(forms.ModelForm):
    class Meta:
        model=PlanejamentoAnual
        fields='__all__'
        exclude=[
            'docente'
        ]


class PlanoDeCursoModelForm(forms.ModelForm):
    class Meta:
        model=PlanoDeCurso
        fields='__all__'
        exclude=[
            'docente'
        ]

class PlanoDeAulaModelForm(forms.ModelForm):
    class Meta:
        model=PlanoDeAula
        fields='__all__'
        exclude=[
            'docente'
        ]
