from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from . import verificacoes as verificar
from django.contrib import messages
from cadastrar.forms import NotasDiscentesModelForm

from .models import Diretor, ViceDiretor, Coordenador, Secretario, Funcionario, Docente, Discente, Turno, Disciplina, Turma, NotasDiscentes,Chamada,Chamada_Discentes,PlanejamentoAnual,PlanoDeCurso,PlanoDeAula
from rolepermissions.decorators import has_permission_decorator
from django.core.paginator import Paginator
from datetime import datetime
from django.db.models import Q
# Create your views here.

######################################################################
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def erro404(request,exception):
    return render(request,'404.html')

@login_required(login_url='login')
def erro403(request,exception):
    messages.error(request,'Você não tem permissão!')
    return redirect('home')
##########################################################################


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_diretor')
def mostrar_diretor(request):
    if request.GET.get('procurar'):
        procurar=request.GET.get('procurar')
        diretores=Diretor.objects.filter(Q(nome__icontains=procurar) | Q(sobrenome__icontains=procurar) 
        | Q(cpf__icontains=procurar) | Q(rg__icontains=procurar)).order_by('user__first_name')
    else:
        diretores = Diretor.objects.all().order_by('user__first_name')
    pagina = request.GET.get('page','1')
    
    diretores_lista=Paginator(diretores,10)
    try:
        diretores=diretores_lista.page(pagina)
    except:
        diretores=diretores_lista.page(1)
    return render(request, 'diretor/diretores.html', {'diretores': diretores})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_vicediretor')
def mostrar_vicediretor(request):
    if request.GET.get('procurar'):
        procurar=request.GET.get('procurar')
        vicediretores=ViceDiretor.objects.filter(Q(nome__icontains=procurar) | Q(sobrenome__icontains=procurar) 
        | Q(cpf__icontains=procurar) | Q(rg__icontains=procurar)).order_by('user__first_name')
    else:
        vicediretores = ViceDiretor.objects.all().order_by('user__first_name')
    pagina= request.GET.get('page','1')
    vicediretores_lista=Paginator(vicediretores,10)
    try:
        vicediretores=vicediretores_lista.page(pagina)
    except:
        vicediretores=vicediretores_lista.page(1)
    return render(request, 'vice-diretor/vice-diretores.html', {'vicediretores': vicediretores})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_coordenador')
def mostrar_coordenador(request):
    if request.GET.get('procurar'):
        procurar=request.GET.get('procurar')
        coordenadores=Coordenador.objects.filter(Q(nome__icontains=procurar) | Q(sobrenome__icontains=procurar) 
        | Q(cpf__icontains=procurar) | Q(rg__icontains=procurar)).order_by('user__first_name')
    else:
        coordenadores = Coordenador.objects.all().order_by('user__first_name')
    pagina=request.GET.get('page','1')
    coordenadores_lista=Paginator(coordenadores,10)
    try:
        coordenadores=coordenadores_lista.page(pagina)
    except:
        coordenadores= coordenadores_lista.page(1)
    return render(request, 'coordenador/coordenadores.html', {'coordenadores': coordenadores})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_secretario')
def mostrar_secretario(request):
    if request.GET.get('procurar'):
        procurar=request.GET.get('procurar')
        secretarios=Secretario.objects.filter(Q(nome__icontains=procurar) | Q(sobrenome__icontains=procurar) 
        | Q(cpf__icontains=procurar) | Q(rg__icontains=procurar)).order_by('user__first_name')
    else:
        secretarios = Secretario.objects.all().order_by('user__first_name')
    pagina=request.GET.get('page','1')
    secretarios_lista=Paginator(secretarios,10)
    try:
        secretarios=secretarios_lista.page(pagina)
    except:
        secretarios=secretarios_lista.page(1)
    return render(request, 'secretario/secretarios.html', {'secretarios': secretarios})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_funcionario')
def mostrar_funcionario(request):
    if request.GET.get('procurar'):
        procurar=request.GET.get('procurar')
        funcionarios=Funcionario.objects.filter(Q(nome__icontains=procurar) | Q(sobrenome__icontains=procurar) 
        | Q(cpf__icontains=procurar) | Q(rg__icontains=procurar)).order_by('user__first_name')
    else:
        funcionarios = Funcionario.objects.all().order_by('user__first_name')
    pagina=request.GET.get('page','1')
    funcionarios_lista=Paginator(funcionarios,10)
    try:
        funcionarios=funcionarios_lista.page(pagina)
    except:
        funcionarios=funcionarios_lista.page(1)
    return render(request, 'funcionario/funcionarios.html', {'funcionarios': funcionarios})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_docente')
def mostrar_docente(request):
    if request.GET.get('procurar'):
        procurar=request.GET.get('procurar')
        docentes=Docente.objects.filter(Q(nome__icontains=procurar) | Q(sobrenome__icontains=procurar) 
        | Q(cpf__icontains=procurar) | Q(rg__icontains=procurar) | Q(disciplinas__nome__icontains=procurar)).order_by('user__first_name')
    else:
        docentes = Docente.objects.all().order_by('user__first_name')
    pagina=request.GET.get('page','1')
    docentes_lista=Paginator(docentes,15)
    try:
        docentes=docentes_lista.page(pagina)
    except:
        docentes= docentes_lista.page(1)
    return render(request, 'docente/docentes.html', {'docentes': docentes})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_discente')
def mostrar_discente(request):
    if request.GET.get('procurar'):
        procurar=request.GET.get('procurar')
        discentes = Discente.objects.filter(Q(nome__icontains=procurar) | Q(sobrenome__icontains=procurar) 
        | Q(cpf__icontains=procurar) | Q(rg__icontains=procurar) | Q(turma__nome__icontains=procurar)).order_by('user__first_name')
    else:
        discentes = Discente.objects.all().order_by('user__first_name')
    pagina=request.GET.get('page','1')
    discentes_lista=Paginator(discentes,20)
    try:
        discentes= discentes_lista.page(pagina)
    except:
        discentes= discentes_lista.page(1)
    return render(request, 'discente/discentes.html', {'discentes': discentes})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_turma')
def mostrar_turma(request):
    if request.GET.get('procurar'):
        procurar=request.GET.get('procurar')
        turmas=Turma.objects.filter(Q(nome__icontains=procurar)).order_by('nome')
    else:
        turmas = Turma.objects.all().order_by('nome')
    pagina=request.GET.get('page','1')
    
    turmas_lista=Paginator(turmas,10)
    try:
        turmas=turmas_lista.page(pagina)
    except:
        turmas=turmas_lista.page(1)
    return render(request, 'turma/turmas.html', {'turmas': turmas})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_turno')
def mostrar_turno(request):
    if request.GET.get('procurar'):
        procurar=request.GET.get('procurar')
        turnos=Turno.objects.filter(Q(nome__icontains=procurar)).order_by('nome')
    else:
        turnos = Turno.objects.all().order_by('nome')
    return render(request, 'turno/turnos.html', {'turnos': turnos})


@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_disciplina')
def mostrar_disciplina(request):
    if request.GET.get('procurar'):
        procurar=request.GET.get('procurar')
        disciplinas=Disciplina.objects.filter(Q(nome__icontains=procurar)).order_by('nome')
    else:
        disciplinas = Disciplina.objects.all().order_by('nome')
    pagina=request.GET.get('page','1')
    disciplinas_lista=Paginator(disciplinas,20)
    try:
        disciplinas=disciplinas_lista.page(pagina)
    except:
        disciplinas= disciplinas_lista.page(1)
    return render(request, 'disciplina/disciplinas.html', {'disciplinas': disciplinas})

@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_planejamento_anual')
def mostrar_planejamento_anual(request):
    if request.GET.get('procurar'):
        procurar=request.GET.get('procurar')
        if request.user.groups.all().first().name=='docente':
            planejamentos = PlanejamentoAnual.objects.filter(Q(docente__user=request.user) | Q(disciplina__nome=procurar)| Q(trimestre=procurar)).order_by('docente__user__first_name')
        else:
            planejamentos = PlanejamentoAnual.objects.filter(Q(disciplina__nome=procurar) | Q(docente__user__first_name=procurar) | Q(trimestre=procurar)).order_by('docente__user__first_name')
    else:
        if request.user.groups.all().first().name=='docente':
            planejamentos = PlanejamentoAnual.objects.filter(Q(docente__user=request.user)).order_by('docente__user__first_name')
        else:
            planejamentos = PlanejamentoAnual.objects.all().order_by('docente__user__first_name')
    pagina=request.GET.get('page','1')
    planejamentos_lista=Paginator(planejamentos,20)
    try:
        planejamentos=planejamentos_lista.page(pagina)
    except:
        planejamentos= planejamentos_lista.page(1)
    return render(request, 'planejamento/planejamentos.html', {'planejamentos': planejamentos})

@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_plano_de_aula')
def mostrar_planos_de_aulas(request):
    if request.GET.get('procurar'):
        procurar=request.GET.get('procurar')
        if request.user.groups.all().first().name=='docente':
            planos = PlanoDeAula.objects.filter(Q(docente__user=request.user) | Q(turma__nome=procurar)| Q(disciplina__nome=procurar)).order_by('docente__user__first_name')
        else:
            planos = PlanoDeAula.objects.filter(Q(turma__nome=procurar)| Q(disciplina__nome=procurar) | Q(docente__user__first_name=procurar)).order_by('docente__user__first_name')
    else:
        if request.user.groups.all().first().name=='docente':
            planos = PlanoDeAula.objects.filter(Q(docente__user=request.user)).order_by('docente__user__first_name')
        else:
            planos = PlanoDeAula.objects.all().order_by('docente__user__first_name')
    pagina=request.GET.get('page','1')
    planos_lista=Paginator(planos,20)
    try:
        planos=planos_lista.page(pagina)
    except:
        planos= planos_lista.page(1)
    return render(request, 'planoAula/planos_de_aulas.html', {'planos': planos})

@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_plano_de_curso')
def mostrar_planos_de_cursos(request):
    if request.GET.get('procurar'):
        procurar=request.GET.get('procurar')
        if request.user.groups.all().first().name=='docente':
            planos = PlanoDeCurso.objects.filter(Q(docente__user=request.user) | Q(area_do_conhecimentos=procurar) | Q(disciplina__nome=procurar)| Q(trimestre=procurar)).order_by('disciplina__nome')
        else:
            planos = PlanoDeCurso.objects.filter(Q(area_do_conhecimentos=procurar) |Q(disciplina__nome=procurar)| Q(trimestre=procurar)| Q(docente__user__first_name=procurar)).order_by('docente__user__first_name')
    else:
        if request.user.groups.all().first().name=='docente':
            planos = PlanoDeCurso.objects.filter(docente__user=request.user).order_by('disciplina__nome')
        else:
            planos = PlanoDeCurso.objects.all().order_by('docente__user__first_name')
    pagina=request.GET.get('page','1')
    planos_lista=Paginator(planos,20)
    try:
        planos=planos_lista.page(pagina)
    except:
        planos= planos_lista.page(1)
    return render(request, 'planoCurso/planos_de_cursos.html', {'planos': planos})

#################################################################################
@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_notas')
def ver_nota_discente(request, id_disciplina, id_discente):
    disciplina = get_object_or_404(Disciplina, id=id_disciplina)
    discente = get_object_or_404(Discente, id=id_discente)
    nota_aluno = get_object_or_404(NotasDiscentes, disciplina=disciplina, discente=discente)
    return render(request,'discente/ver_nota_discente.html',{'nota':nota_aluno})
    
@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_notas')
def edt_nota_discente(request, id_disciplina, id_discente):
    disciplina = get_object_or_404(Disciplina, id=id_disciplina)
    if not request.user.is_superuser:
        try:
            docente=get_object_or_404(Docente,user=request.user)
            disciplinas= docente.disciplinas.all()
            if not disciplina in disciplinas:
                messages.error(request,'Você não tem acesso a essa disciplina!')
                return redirect('detalhes_discente',id_discente)
        except:
            messages.error(request,'Você não é um Docente!')
            return redirect('home')
    discente = get_object_or_404(Discente, id=id_discente)
    nota_aluno = get_object_or_404(
        NotasDiscentes, disciplina=disciplina, discente=discente)
    if request.method == 'POST':
        form = NotasDiscentesModelForm(
            request.POST or None, instance=nota_aluno)
        if form.is_valid():
            nota = form.save()
            nota.media = (nota.nota1+nota.nota2+nota.nota3)/3
            nota.media = round(nota.media, 2)
            nota.save()
            if nota.faltas>nota.disciplina.carga_horaria*0.25:
                nota.situacao='Reprovado por falta'
                nota.discente.situacao='Reprovado por falta'
                nota.discente.save()
                nota.save()
            else:
                nota.situacao='Em andamento'
                nota.discente.situacao='Em andamento'
                nota.discente.save()
                nota.save()
            messages.success(
                request, f'Nota de {disciplina.nome} atualizada com sucesso!')
            return redirect('detalhes_discente', id_discente)
        else:
            messages.error(request, 'Erro ao alterar nota!')
            return redirect('detalhes_discente', id_discente)

    form = NotasDiscentesModelForm(instance=nota_aluno)
    return render(request, 'discente/editar_nota_discente.html', {'form': form, 'nota': nota_aluno})


@login_required(login_url='login')
@has_permission_decorator(permission_name='fazer_chamada')
def fazer_chamada(request,id_turma):
    turma = get_object_or_404(Turma, pk=id_turma)
    try:
        docente=get_object_or_404(Docente,user=request.user)
    except:
        messages.error(request,'Você não é um Docente!')
        return redirect('home')
    disciplinas=docente.disciplinas.all()
    if not disciplinas:
        messages.error(request,'Você não está vinculado a nenhuma disciplina!')
        return redirect('detalhes_turma',turma.id)
    discentes=Discente.objects.filter(turma=turma).order_by('user__first_name')
    if request.method=='POST':
        faltas=request.POST.getlist('falta')
        disciplina=request.POST.get('disciplina')
        if not disciplina:
            messages.error(request,'Você não selecionou nenhuma disciplina!')
            return redirect('fazer_chamada',turma.id)
        disciplina=get_object_or_404(Disciplina,pk=disciplina)
        if not disciplina in docente.disciplinas.all():
            messages.error(request,'Você selecionou uma disciplina que não é sua!')
            return redirect('fazer_chamada',turma.id)
        chamada=Chamada.objects.create(
            turma=turma,
            disciplina=disciplina
        )
        for i in range(len(discentes)):
            nota=get_object_or_404(NotasDiscentes,discente=discentes[i],disciplina=disciplina)
            nota.faltas+=int(faltas[i])
            nota.save()
            if nota.faltas>nota.disciplina.carga_horaria*0.25:
                nota.situacao='Reprovado por falta'
                nota.discente.situacao='Reprovado por falta'
                nota.discente.save()
                nota.save()
            chamada_discente=Chamada_Discentes.objects.create(
                discente=discentes[i],
                quant_faltas=faltas[i],
                chamada=chamada
            )
            chamada_discente.save()
        messages.success(request,'Chamada realizada com sucesso.')
        return redirect('detalhes_turma',id_turma)

        
    return render(request,'docente/fazer_chamada.html',{'turma':turma,'discentes':discentes,'disciplinas':disciplinas})



@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_chamadas')
def mostrar_chamadas(request,id_turma):
    turma=get_object_or_404(Turma,pk=id_turma)
    chamadas=Chamada.objects.filter(turma=turma).order_by('data_da_chamada')
    return render(request,'turma/chamadas.html',{'chamadas':chamadas,'turma':turma})

@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_chamadas')
def detalhes_chamada(request,id_chamada):
    chamada=get_object_or_404(Chamada,pk=id_chamada)
    return render(request,'turma/detalhes_chamada.html',{'chamada':chamada})
################################################################
@login_required(login_url='login')
@has_permission_decorator(permission_name='situacao_discentes')
def situacao_discentes(request,id_turma):
    if not request.user.is_superuser:
        data=datetime.now()
        if data.strftime('%b') != 'Dec':
            messages.warning(request,'Função liberada somente no fim do ano letivo')
            return redirect('detalhes_turma',id_turma)
    turma=get_object_or_404(Turma,pk=id_turma)
    discentes=Discente.objects.filter(turma=turma)
    for discente in discentes:
        notas=NotasDiscentes.objects.filter(discente=discente)
        quant_pf=0
        reprovado=False
        reprovado_falta=False
        for nota in notas:
            nota.media=(nota.nota1+nota.nota2+nota.nota3)/3
            nota.media=round(nota.media,2)
            nota.save()
            if nota.media<5:
                nota.situacao='Prova Final'
                nota.save()
                quant_pf+=1
            else:
                nota.situacao='Aprovado'
                nota.save()
            if nota.faltas>nota.disciplina.carga_horaria*0.25:
                nota.situacao='Reprovado por falta'
                nota.save()
                reprovado_falta=True
        if quant_pf==0:
            discente.situacao='Aprovado'
            discente.save()
        elif quant_pf<4:
            discente.situacao='Prova Final'
            discente.save()
        elif quant_pf>=4:
            reprovado=True
        if reprovado:
            discente.situacao='Reprovado'
            discente.save()
        elif reprovado_falta:
            discente.situacao='Reprovado por falta'
            discente.save()
    messages.success(request,'Situação de todos os alunos dessa turma verificados!')
    return redirect('detalhes_turma',id_turma)

@login_required(login_url='login')
@has_permission_decorator(permission_name='situacao_discentes')
def situacao_discente(request,id_discente):
    if not request.user.is_superuser:
        data=datetime.now()
        if data.strftime('%b') != 'Dec':
            messages.warning(request,'Função liberada somente no fim do ano letivo')
            return redirect('detalhes_discente',id_discente)
    discente=get_object_or_404(Discente,pk=id_discente)
    try:
        notas=NotasDiscentes.objects.filter(discente=discente)
        quant_pf=0
        reprovado=False
        reprovado_falta=False
        for nota in notas:
            nota.media=(nota.nota1+nota.nota2+nota.nota3)/3
            nota.media=round(nota.media,2)
            nota.save()
            if nota.media<5:
                nota.situacao='Prova Final'
                nota.save()
                quant_pf+=1
            else:
                nota.situacao='Aprovado'
                nota.save()
            if nota.faltas>nota.disciplina.carga_horaria*0.25:
                nota.situacao='Reprovado por falta'
                nota.save()
                reprovado_falta=True
        if quant_pf==0:
            discente.situacao='Aprovado'
            discente.save()
        elif quant_pf<4:
            discente.situacao='Prova Final'
            discente.save()
        elif quant_pf>=4:
            reprovado=True
        if reprovado:
            discente.situacao='Reprovado'
            discente.save()
        elif reprovado_falta:
            discente.situacao='Reprovado por falta'
            discente.save()
        messages.success(request,'Situação do aluno verificado!')
        return redirect('detalhes_discente',id_discente)
    except:
        messages.error(request,'Algo deu erro na verificação da situação do aluno!')
        return redirect('detalhes_discente',id_discente)

######################################################
@login_required(login_url='login')
@has_permission_decorator(permission_name='ver_notas_aluno')
def mostrar_notas(request):
    try:
        discente=get_object_or_404(Discente,user=request.user)
    except:
        messages.error(request,'Você não é um discente!')
        return redirect('home')
    notas=NotasDiscentes.objects.filter(discente=discente)
    return render(request,'discente/detalhes_notas.html',{'notas':notas,'discente':discente})