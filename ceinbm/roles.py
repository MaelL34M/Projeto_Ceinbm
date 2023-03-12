from rolepermissions.roles import AbstractUserRole


class Diretor(AbstractUserRole):
    available_permissions = {
        'modificar_diretor': True,'ver_diretor': True,'apagar_diretor': True,
        'modificar_vicediretor': True,'ver_vicediretor': True,'apagar_vicediretor': True,
        'modificar_coordenador': True,'ver_coordenador': True,'apagar_coordenador': True,
        'modificar_secretario': True,'ver_secretario': True,'apagar_secretario': True,
        'modificar_funcionario': True,'ver_funcionario': True,'apagar_funcionario': True,
        'modificar_docente': True,'ver_docente': True,'apagar_docente': True,
        'modificar_discente': True,'ver_discente': True,'apagar_discente': True,
        'modificar_notas': False,'ver_notas': True,'apagar_notas': True,
        'modificar_turno': True,'ver_turno': True,'apagar_turno': True,
        'modificar_turma': True,'ver_turma': True,'apagar_turma': True,'ver_chamadas': True,
        'modificar_disciplina':True,'ver_disciplina':True,'apagar_disciplina': True,
        'modificar_perfil': True,'ver_perfil': True, 'apagar_perfil': True,
        'situacao_discentes': True,
        'ver_planejamento_anual': True,'ver_plano_de_aula': True,'ver_plano_de_curso': True,
    }


class Vicediretor(AbstractUserRole):
    available_permissions = {
        'modificar_vicediretor': True,'ver_vicediretor': True,'apagar_vicediretor': True,
        'modificar_coordenador': True,'ver_coordenador': True,'apagar_coordenador': True,
        'modificar_secretario': True,'ver_secretario': True,'apagar_secretario': True,
        'modificar_funcionario': True,'ver_funcionario': True,'apagar_funcionario': True,
        'modificar_docente': True,'ver_docente': True,'apagar_docente': True,
        'modificar_discente': True,'ver_discente': True,'apagar_discente': True,
        'modificar_notas': False,'ver_notas': True,'apagar_notas': True,
        'modificar_turno': True,'ver_turno': True,'apagar_turno': False,
        'modificar_turma': True,'ver_turma': True,'apagar_turma': True,'ver_chamadas': True,
        'modificar_disciplina':True,'ver_disciplina':True,'apagar_disciplina': True,
        'modificar_perfil': True,'ver_perfil': True, 'apagar_perfil': True,
        'situacao_discentes': True,
        'ver_planejamento_anual': True,'ver_plano_de_aula': True,'ver_plano_de_curso': True,
    }


class Coordenador(AbstractUserRole):
    available_permissions = {
        'modificar_coordenador': True,'ver_coordenador': True,'apagar_coordenador': True,
        'modificar_secretario': True,'ver_secretario': True,'apagar_secretario': True,
        'modificar_funcionario': True,'ver_funcionario': True,'apagar_funcionario': True,
        'modificar_docente': True,'ver_docente': True,'apagar_docente': True,
        'modificar_discente': True,'ver_discente': True,'apagar_discente': True,
        'modificar_notas': False,'ver_notas': True,'apagar_notas': True,
        'modificar_turno': True,'ver_turno': True,'apagar_turno': False,
        'modificar_turma': True,'ver_turma': True,'apagar_turma': True,'ver_chamadas': True,
        'modificar_disciplina':True,'ver_disciplina':True,'apagar_disciplina': True,
        'modificar_perfil': True,'ver_perfil': True, 'apagar_perfil': True, 
        'situacao_discentes': True,
        'ver_planejamento_anual': True,'ver_plano_de_aula': True,'ver_plano_de_curso': True,
    }


class Secretario(AbstractUserRole):
    available_permissions = {
        'modificar_funcionario': True,'ver_funcionario': True,'apagar_funcionario': True,
        'modificar_docente': True,'ver_docente': True,'apagar_docente': True,
        'modificar_discente': True,'ver_discente': True,'apagar_discente': False,
        'ver_notas': True,'apagar_notas': False,
        'modificar_turno': True,'ver_turno': True,'apagar_turno': False,
        'modificar_turma': True,'ver_turma': True,'apagar_turma': True,'ver_chamadas': True,
        'modificar_disciplina':True,'ver_disciplina':True,'apagar_disciplina': True,
        'modificar_perfil': True,'ver_perfil': True, 'apagar_perfil': True,
    }


class Funcionario(AbstractUserRole):
    available_permissions = {
        'modificar_perfil': True,'ver_perfil': True
    }


class Docente(AbstractUserRole):
    available_permissions = {
        'ver_turno': True,'ver_turma': True,'ver_discente': True,'ver_chamadas': True,
        'modificar_notas': True, 'fazer_chamada': True,
        'fazer_planejamento_anual': True,'fazer_plano_de_aula': True,'fazer_plano_de_curso': True,
        'ver_planejamento_anual': True,'ver_plano_de_aula': True,'ver_plano_de_curso': True,
        'modificar_perfil': True,'ver_perfil': True,
        'situacao_discentes': True,
    }


class Discente(AbstractUserRole):
    available_permissions = {
        'ver_perfil': True, 'ver_notas_aluno': True
    }
