from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_permission_decorator
from django.contrib import messages
from principal.models import Diretor, ViceDiretor, Coordenador, Secretario, Funcionario, Docente, Discente, Turno, Disciplina, Turma, NotasDiscentes,Chamada,Chamada_Discentes,PlanejamentoAnual,PlanoDeCurso,PlanoDeAula
# Create your views here.
@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_diretor')
def detalhes_diretor(request, id):
    diretor = get_object_or_404(Diretor, pk=id)
    return render(request, 'detalhes_diretor.html', {'diretor': diretor})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_vicediretor')
def detalhes_vicediretor(request, id):
    vicediretor = get_object_or_404(ViceDiretor, pk=id)
    return render(request, 'detalhes_vicediretor.html', {'vicediretor': vicediretor})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_coordenador')
def detalhes_coordenador(request, id):
    coordenador = get_object_or_404(Coordenador, pk=id)
    return render(request, 'detalhes_coordenador.html', {'coordenador': coordenador})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_secretario')
def detalhes_secretario(request, id):
    secretario = get_object_or_404(Secretario, pk=id)
    return render(request, 'detalhes_secretario.html', {'secretario': secretario})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_funcionario')
def detalhes_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    return render(request, 'detalhes_funcionario.html', {'funcionario': funcionario})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_docente')
def detalhes_docente(request, id):
    docente = get_object_or_404(Docente, pk=id)
    disciplinas = docente.disciplinas.all()

    return render(request, 'detalhes_docente.html', {'docente': docente, 'disciplinas': disciplinas})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_discente')
def detalhes_discente(request, id):
    discente = get_object_or_404(Discente, pk=id)
    notas = NotasDiscentes.objects.filter(discente=discente)
    return render(request, 'detalhes_discente.html', {'discente': discente, 'notas': notas})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_turno')
def detalhes_turno(request, id):
    turno = get_object_or_404(Turno, pk=id)
    turmas = Turma.objects.filter(turno=turno).order_by('nome')
    num_turmas = turmas.count()
    num_discentes = 0
    for turma in turmas:
        num_discentes += Discente.objects.filter(turma=turma).count()
    return render(request, 'detalhes_turno.html', {'turno': turno, 'turmas': turmas, 'num_turmas': num_turmas, 'num_discentes': num_discentes})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_turma')
def detalhes_turma(request, id):
    turma = get_object_or_404(Turma, pk=id)
    discentes = Discente.objects.filter(turma=turma).order_by('nome')
    num_discentes = discentes.count()
    return render(request, 'detalhes_turma.html', {'turma': turma, 'discentes': discentes, 'num_discentes': num_discentes})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_disciplina')
def detalhes_disciplina(request, id):
    disciplina = get_object_or_404(Disciplina, pk=id)
    docentes = Docente.objects.filter(disciplinas=disciplina).order_by('nome')
    return render(request, 'detalhes_disciplina.html', {'disciplina': disciplina, 'docentes': docentes})

@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_planejamento_anual')
def detalhes_planejamento_anual(request, id):
    planejamento = get_object_or_404(PlanejamentoAnual, pk=id)
    return render(request, 'detalhes_planejamento_anual.html', {'planejamento': planejamento})

@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_plano_de_curso')
def detalhes_plano_de_curso(request, id):
    plano = get_object_or_404(PlanoDeCurso, pk=id)
    return render(request, 'detalhes_planejamento_anual.html', {'plano': plano})

@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_plano_de_aula')
def detalhes_plano_de_aula(request, id):
    plano = get_object_or_404(PlanoDeAula, pk=id)
    return render(request, 'detalhes_planejamento_anual.html', {'plano': plano})