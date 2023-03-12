from principal.models import Diretor,ViceDiretor,Coordenador,Secretario,Funcionario,Docente,Discente,Disciplina,Turma,Turno,NotasDiscentes
from django import forms


class DiretorEditarModelForm(forms.ModelForm):
    class Meta:
        model=Diretor
        fields='__all__'
        exclude=[
            'user',
            'cargo',
            'senha',
            'email'
        ]
class ViceDiretorEditarModelForm(forms.ModelForm):
    class Meta:
        model=ViceDiretor
        fields='__all__'
        exclude=[
            'user',
            'cargo',
            'email',
            'senha'
        ]

class CoordenadorEditarModelForm(forms.ModelForm):
    class Meta:
        model=Coordenador
        fields='__all__'
        exclude=[
            'user',
            'cargo',
            'email',
            'senha'
        ]

class SecretarioEditarModelForm(forms.ModelForm):
    class Meta:
        model=Secretario
        fields='__all__'
        exclude=[
            'user',
            'cargo',
            'email',
            'senha'
        ]
class FuncionarioEditarModelForm(forms.ModelForm):
    class Meta:
        model=Funcionario
        fields='__all__'
        exclude=[
            'user',
            'email',
            'senha'
        ]
class DocenteEditarModelForm(forms.ModelForm):
    class Meta:
        model=Docente
        fields='__all__'
        exclude=[
            'user',
            'cargo',
            'documentos',
            'email',
            'senha'
        ]
        widgets={
            'disciplinas':forms.CheckboxSelectMultiple
        }
class DiscenteEditarModelForm(forms.ModelForm):
    class Meta:
        model=Discente
        fields='__all__'
        exclude=[
            'user',
            'cargo',
            'disciplinas',
            'email',
            'senha'
        ]