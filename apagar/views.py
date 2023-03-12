from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_permission_decorator
from django.contrib import messages
from principal.models import Diretor, ViceDiretor, Coordenador, Secretario, Funcionario, Docente, Discente, Turno, Disciplina, Turma, NotasDiscentes,Chamada,Chamada_Discentes,PlanejamentoAnual,PlanoDeCurso,PlanoDeAula

# Create your views here.
@login_required(login_url='login')
@has_permission_decorator(permission_name='apagar_diretor')
def del_diretor(request, id):
    try:
        diretor = get_object_or_404(Diretor, pk=id)
        diretor.delete()
        messages.success(request, 'Deletado com sucesso!')
        return redirect('mostrar_diretor')
    except:
        messages.error(request, 'Falha ao deletar!')
        return redirect('mostrar_diretor')


@login_required(login_url='login')
@has_permission_decorator(permission_name='apagar_vicediretor')
def del_vicediretor(request, id):
    try:
        vice = get_object_or_404(ViceDiretor, pk=id)
        vice.delete()
        messages.success(request, 'Deletado com sucesso!')
        return redirect('mostrar_vicediretor')
    except:
        messages.error(request, 'Falha ao deletar!')
        return redirect('mostrar_vicediretor')


@login_required(login_url='login')
@has_permission_decorator(permission_name='apagar_coordenador')
def del_coordenador(request, id):
    try:
        coor = get_object_or_404(Coordenador, pk=id)
        coor.delete()
        messages.success(request, 'Deletado com sucesso!')
        return redirect('mostrar_coordenador')
    except:
        messages.error(request, 'Falha ao deletar!')
        return redirect('mostrar_coordenador')


@login_required(login_url='login')
@has_permission_decorator(permission_name='apagar_secretario')
def del_secretario(request, id):
    try:
        secretario = get_object_or_404(Secretario, pk=id)
        secretario.delete()
        messages.success(request, 'Deletado com sucesso!')
        return redirect('mostrar_secretario')
    except:
        messages.error(request, 'Falha ao deletar!')
        return redirect('mostrar_secretario')


@login_required(login_url='login')
@has_permission_decorator(permission_name='apagar_funcionario')
def del_funcionario(request, id):
    try:
        func = get_object_or_404(Funcionario, pk=id)
        func.delete()
        messages.success(request, 'Deletado com sucesso!')
        return redirect('mostrar_funcionario')
    except:
        messages.error(request, 'Falha ao deletar!')
        return redirect('mostrar_funcionario')


@login_required(login_url='login')
@has_permission_decorator(permission_name='apagar_docente')
def del_docente(request, id):
    try:
        docente = get_object_or_404(Docente, pk=id)
        docente.delete()
        messages.success(request, 'Deletado com sucesso!')
        return redirect('mostrar_docente')
    except:
        messages.error(request, 'Falha ao deletar!')
        return redirect('mostrar_docente')


@login_required(login_url='login')
@has_permission_decorator(permission_name='apagar_discente')
def del_discente(request, id):
    try:
        discente = get_object_or_404(Discente, pk=id)
        discente.delete()
        messages.success(request, 'Deletado com sucesso!')
        return redirect('mostrar_discente')
    except:
        messages.error(request, 'Falha ao deletar!')
        return redirect('mostrar_discente')


@login_required(login_url='login')
@has_permission_decorator(permission_name='apagar_turno')
def del_turno(request, id):
    try:
        turno = get_object_or_404(Turno, pk=id)
        turno.delete()
        messages.success(request, 'Deletado com sucesso!')
        return redirect('mostrar_turno')
    except:
        messages.error(request, 'Falha ao deletar!')
        return redirect('mostrar_turno')


@login_required(login_url='login')
@has_permission_decorator(permission_name='apagar_turma')
def del_turma(request, id):
    try:
        turma = get_object_or_404(Turma, pk=id)
        turma.delete()
        messages.success(request, 'Deletado com sucesso!')
        return redirect('mostrar_turma')
    except:
        messages.error(request, 'Falha ao deletar!')
        return redirect('mostrar_turma')


@login_required(login_url='login')
@has_permission_decorator(permission_name='apagar_disciplina')
def del_disciplina(request, id):
    try:
        disciplina = get_object_or_404(Disciplina, pk=id)
        disciplina.delete()
        messages.success(request, 'Deletado com sucesso!')
        return redirect('mostrar_disciplina')
    except:
        messages.error(request, 'Falha ao deletar!')
        return redirect('mostrar_disciplina')
@login_required(login_url='login')
@has_permission_decorator(permission_name='apagar_planejamento')
def del_planejamento_anual(request, id):
    try:
        planejamento = get_object_or_404(PlanejamentoAnual, pk=id)
        planejamento.delete()
        messages.success(request, 'Deletado com sucesso!')
        return redirect('mostrar_planejamento')
    except:
        messages.error(request, 'Falha ao deletar!')
        return redirect('mostrar_planejamento')

@login_required(login_url='login')
@has_permission_decorator(permission_name='apagar_planejamento')
def del_plano_de_aula(request, id):
    try:
        plano = get_object_or_404(PlanoDeAula, pk=id)
        plano.delete()
        messages.success(request, 'Deletado com sucesso!')
        return redirect('mostrar_plano_de_aula')
    except:
        messages.error(request, 'Falha ao deletar!')
        return redirect('mostrar_plano_de_aula')

@login_required(login_url='login')
@has_permission_decorator(permission_name='apagar_planejamento')
def del_plano_de_curso(request, id):
    try:
        plano = get_object_or_404(PlanoDeCurso, pk=id)
        plano.delete()
        messages.success(request, 'Deletado com sucesso!')
        return redirect('mostrar_plano_de_curso')
    except:
        messages.error(request, 'Falha ao deletar!')
        return redirect('mostrar_plano_de_curso')

