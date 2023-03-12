from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rolepermissions.decorators import has_permission_decorator
from principal.models import Diretor, ViceDiretor, Coordenador, Secretario, Funcionario, Docente, Discente, Turno, Disciplina, Turma, NotasDiscentes,Chamada,Chamada_Discentes,PlanejamentoAnual,PlanoDeCurso,PlanoDeAula
from .formsEditar import DiretorEditarModelForm,ViceDiretorEditarModelForm,CoordenadorEditarModelForm,SecretarioEditarModelForm, FuncionarioEditarModelForm, \
    DocenteEditarModelForm,DiscenteEditarModelForm
from cadastrar.forms import TurmaModelForm,TurnoModelForm,DisciplinaModelForm,PlanejamentoAnualModelForm,PlanoDeCursoModelForm,PlanoDeAulaModelForm
from principal import verificacoes as verificar
# Create your views here.
@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_diretor')
def edt_diretor(request, id):
    diretor = get_object_or_404(Diretor, pk=id)
    form = DiretorEditarModelForm(
        request.POST or None, request.FILES or None, instance=diretor)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        if verificar.verificacao_geral_editar(nome, sobrenome) != False:
            messages.error(
                request, verificar.verificacao_geral(nome, sobrenome))
            return redirect('detalhes_diretor', id)
        try:
            if form.is_valid():
                diretor = form.save()
                diretor.user.first_name = nome
                diretor.user.last_name = sobrenome
                diretor.user.save()
                messages.success(request, f'{nome} editado com sucesso!')
                return redirect('detalhes_diretor', id)
            else:
                messages.error(request, 'Formulário inválido!')
                return redirect('detalhes_diretor', id)
        except:
            messages.error(request, 'Algo deu erro na edição!')
            return redirect('detalhes_diretor', id)
    return render(request, 'editar_diretor.html', {'form': form, 'id': id})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_vicediretor')
def edt_vicediretor(request, id):
    vicediretor = get_object_or_404(ViceDiretor, pk=id)
    form = ViceDiretorEditarModelForm(
        request.POST or None, request.FILES or None, instance=vicediretor)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        if verificar.verificacao_geral_editar(nome, sobrenome) != False:
            messages.error(
                request, verificar.verificacao_geral(nome, sobrenome))
            return redirect('detalhes_vicediretor', id)
        try:
            if form.is_valid():
                vicediretor = form.save()
                vicediretor.user.first_name = nome
                vicediretor.user.last_name = sobrenome
                vicediretor.user.save()
                messages.success(request, f'{nome} editado com sucesso!')
                return redirect('detalhes_vicediretor', id)
            else:
                messages.error(request, 'Formulário inválido!')
                return redirect('detalhes_vicediretor', id)
        except:
            messages.error(request, 'Algo deu erro na edição!')
            return redirect('detalhes_vicediretor', id)
    return render(request, 'editar_vicediretor.html', {'form': form, 'id': id})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_coordenador')
def edt_coordenador(request, id):
    coordenador = get_object_or_404(Coordenador, pk=id)
    form = CoordenadorEditarModelForm(
        request.POST or None, request.FILES or None, instance=coordenador)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        if verificar.verificacao_geral_editar(nome, sobrenome) != False:
            messages.error(
                request, verificar.verificacao_geral(nome, sobrenome))
            return redirect('detalhes_coordenador', id)
        try:
            if form.is_valid():
                coordenador = form.save()
                coordenador.user.first_name = nome
                coordenador.user.last_name = sobrenome
                coordenador.user.save()
                messages.success(request, f'{nome} editado com sucesso!')
                return redirect('detalhes_coordenador', id)
            else:
                messages.error(request, 'Formulário inválido!')
                return redirect('detalhes_coordenador', id)
        except:
            messages.error(request, 'Algo deu erro na edição!')
            return redirect('detalhes_coordenador', id)
    return render(request, 'editar_coordenador.html', {'form': form, 'id': id})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_secretario')
def edt_secretario(request, id):
    secretario = get_object_or_404(Secretario, pk=id)
    form = SecretarioEditarModelForm(
        request.POST or None, request.FILES or None, instance=secretario)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        if verificar.verificacao_geral_editar(nome, sobrenome) != False:
            messages.error(
                request, verificar.verificacao_geral(nome, sobrenome))
            return redirect('detalhes_secretario', id)
        try:
            if form.is_valid():
                secretario = form.save()
                secretario.user.first_name = nome
                secretario.user.last_name = sobrenome
                secretario.user.save()
                messages.success(request, f'{nome} editado com sucesso!')
                return redirect('detalhes_secretario', id)
            else:
                messages.error(request, 'Formulário inválido!')
                return redirect('detalhes_secretario', id)
        except:
            messages.error(request, 'Algo deu erro na edição!')
            return redirect('detalhes_secretario', id)
    return render(request, 'editar_secretario.html', {'form': form, 'id': id})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_funcionario')
def edt_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    form = FuncionarioEditarModelForm(
        request.POST or None, request.FILES or None, instance=funcionario)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        if verificar.verificacao_geral_editar(nome, sobrenome) != False:
            messages.error(
                request, verificar.verificacao_geral(nome, sobrenome))
            return redirect('detalhes_funcionario', id)
        try:
            if form.is_valid():
                funcionario = form.save()
                funcionario.user.first_name = nome
                funcionario.user.last_name = sobrenome
                funcionario.user.save()
                messages.success(request, f'{nome} editado com sucesso!')
                return redirect('detalhes_funcionario', id)
            else:
                messages.error(request, 'Formulário inválido!')
                return redirect('detalhes_funcionario', id)
        except:
            messages.error(request, 'Algo deu erro na edição!')
            return redirect('detalhes_funcionario', id)
    return render(request, 'editar_funcionario.html', {'form': form, 'id': id})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_docente')
def edt_docente(request, id):
    docente = get_object_or_404(Docente, pk=id)
    form = DocenteEditarModelForm(
        request.POST or None, request.FILES or None, instance=docente)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        if verificar.verificacao_geral_editar(nome, sobrenome) != False:
            messages.error(
                request, verificar.verificacao_geral(nome, sobrenome))
            return redirect('detalhes_docente', id)
        try:
            if form.is_valid():
                docente = form.save()
                docente.user.first_name = nome
                docente.user.last_name = sobrenome
                docente.user.save()
                messages.success(request, f'{nome} editado com sucesso!')
                return redirect('detalhes_docente', id)
            else:
                messages.error(request, 'Formulário inválido!')
                return redirect('detalhes_docente', id)
        except:
            messages.error(request, 'Algo deu erro na edição!')
            return redirect('detalhes_docente', id)
    return render(request, 'editar_docente.html', {'form': form, 'id': id})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_discente')
def edt_discente(request, id):
    discente = get_object_or_404(Discente, pk=id)
    form = DiscenteEditarModelForm(
        request.POST or None, request.FILES or None, instance=discente)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        if verificar.verificacao_geral_editar(nome, sobrenome) != False:
            messages.error(
                request, verificar.verificacao_geral(nome, sobrenome))
            return redirect('detalhes_discente', id)
        try:
            if form.is_valid():
                discente = form.save()
                discente.user.first_name = nome
                discente.user.last_name = sobrenome
                discente.user.save()
                messages.success(request, f'{nome} editado com sucesso!')
                return redirect('detalhes_discente', id)
            else:
                messages.error(request, 'Formulário inválido!')
                return redirect('detalhes_discente', id)
        except:
            messages.error(request, 'Algo deu erro na edição!')
            return redirect('detalhes_discente', id)
    return render(request, 'editar_discente.html', {'form': form, 'id': id})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_turno')
def edt_turno(request, id):
    turno = get_object_or_404(Turno, pk=id)
    form = TurnoModelForm(request.POST or None, instance=turno)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if not nome:
            messages.error(request, 'Nome do turno vazio!')
            return redirect('edt_turno', id)
        if nome.strip() == '':
            messages.error(request, 'Nome do turno vazio!')
            return redirect('edt_turno', id)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, f'{nome} editado com sucesso!')
                return redirect('detalhes_turno', id)
            else:
                messages.error(request, 'Formulário inválido!')
                return redirect('cad_turno', id)
        except:
            messages.error(request, 'Algo deu erro no Cadastro!')
            return redirect('cad_turno', id)

    return render(request, 'editar_turno.html', {'form': form, 'id': id})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_turma')
def edt_turma(request, id):
    turma = get_object_or_404(Turma, pk=id)
    form = TurmaModelForm(request.POST or None, instance=turma)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if not nome:
            messages.error(request, 'Nome da turma vazio!')
            return redirect('edt_turma', id)
        if nome.strip() == '':
            messages.error(request, 'Nome da turma vazio!')
            return redirect('edt_turma', id)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, f'{nome} editado com sucesso!')
                return redirect('detalhes_turma', id)
            else:
                messages.error(request, 'Formulário inválido!')
                return redirect('edt_turma', id)
        except:
            messages.error(request, 'Algo deu erro na edição!')
            return redirect('edt_turma', id)

    return render(request, 'editar_turma.html', {'form': form,'id':id})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_disciplina')
def edt_disciplina(request, id):
    disciplina = get_object_or_404(Disciplina, pk=id)
    form = DisciplinaModelForm(request.POST or None, instance=disciplina)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if not nome:
            messages.error(request, 'Nome da disciplina vazio!')
            return redirect('edt_disciplina', id)
        if nome.strip() == '':
            messages.error(request, 'Nome da disciplina vazio!')
            return redirect('edt_disciplina', id)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, f'{nome} editado com sucesso!')
                return redirect('detalhes_disciplina', id)
            else:
                messages.error(request, 'Formulário inválido!')
                return redirect('edt_disciplina', id)
        except:
            messages.error(request, 'Algo deu erro no Cadastro!')
            return redirect('edt_disciplina', id)

    return render(request, 'editar_disciplina.html', {'form': form,'id':id})

@login_required(login_url='login')
@has_permission_decorator(permission_name='fazer_planejamento_anual')
def edt_planejamento_anual(request,id):
    planejamento=get_object_or_404(PlanejamentoAnual)
    if planejamento.docente.user!=request.user:
        messages.error(request,'Você não possui acesso a esse planejamento')
        return redirect('mostrar_planajemento_anual')
    form=PlanejamentoAnualModelForm(request.POST or None,instance=planejamento)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Plano anual editado com sucesso!')
            return redirect('mostrar_planajemento_anual')
        else:
            messages.error(request,'Formulário não é valido')
            return render(request, 'editar_planejamento_anual.html',{'form':form,'id':id})
    return render(request, 'editar_planejamento_anual.html',{'form':form,'id':id})

@login_required(login_url='login')
@has_permission_decorator(permission_name='fazer_plano_de_aula')
def edt_plano_de_aula(request,id):
    plano=get_object_or_404(PlanoDeAula)
    if plano.docente.user!=request.user:
        messages.error(request,'Você não possui acesso a esse plano de aula')
        return redirect('mostrar_plano_de_aula')
    form=PlanoDeAulaModelForm(request.POST or None,instance=plano)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Plano de aula cadastrado com sucesso!')
            return redirect('mostrar_plano_de_aula')
        else:
            messages.error(request,'Formulário não é valido')
            return render(request, 'editar_plano_de_aula.html',{'form':form,'id':id})
    return render(request, 'editar_plano_de_aula.html',{'form':form,'id':id})

@login_required(login_url='login')
@has_permission_decorator(permission_name='fazer_plano_de_curso')
def edt_plano_de_curso(request,id):
    plano=get_object_or_404(PlanoDeCurso)
    if plano.docente.user!=request.user:
        messages.error(request,'Você não possui acesso a esse plano de curso')
        return redirect('mostrar_plano_de_curso')
    form=PlanoDeCursoModelForm(request.POST or None,instance=plano)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Plano de curso cadastrado com sucesso!')
            return redirect('mostrar_plano_de_curso')
        else:
            messages.error(request,'Formulário não é valido')
            return render(request, 'editar_plano_de_curso.html',{'form':form,'id':id})
    return render(request, 'editar_plano_de_curso.html',{'form':form,'id':id})