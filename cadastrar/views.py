from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_permission_decorator
from rolepermissions.roles import assign_role
from principal import verificacoes as verificar
from . import formatacoes
from django.contrib import messages
from .forms import DiretorModelForm, ViceDiretorModelForm, CoordenadorModelForm, SecretarioModelForm, \
    FuncionarioModelForm, DocenteModelForm, DiscenteModelForm, TurmaModelForm, TurnoModelForm, DisciplinaModelForm,PlanejamentoAnualModelForm,PlanoDeAulaModelForm,PlanoDeCursoModelForm

from principal.models import Docente, Discente, Turno, Disciplina, Turma, NotasDiscentes
# Create your views here.


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_diretor')
def cad_diretor(request):
    form = DiretorModelForm(
                request.POST or None, request.FILES or None)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if verificar.verificacao_geral(nome, sobrenome, email=email, senha=senha) != False:
            messages.error(request, verificar.verificacao_geral(
                nome, sobrenome, email=email, senha=senha))
            return redirect('cad_diretor')
        try:
            user = User.objects.create_user(
                username=email,
                first_name=nome,
                last_name=sobrenome,
                email=email,
                password=senha
            )
            user.save()
            assign_role(user, 'diretor')
            if form.is_valid():
                diretor = form.save()
                diretor.save()
                diretor.user = user
                diretor.save()
                messages.success(request, f'{nome} cadastrado com sucesso!')
                return redirect('mostrar_diretor')
            else:
                if user:
                    user.delete()
                messages.error(request, 'Formulário inválido!')
                return redirect('cad_diretor', {'form': form})
        except:
            if user:
                user.delete()
            messages.error(request, 'Algo deu erro no Cadastro!')
            return redirect('cad_diretor', {'form': form})
    return render(request, 'cadastrar_diretor.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_vicediretor')
def cad_vicediretor(request):
    form = ViceDiretorModelForm(
                request.POST or None, request.FILES or None)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if verificar.verificacao_geral(nome, sobrenome, email=email, senha=senha) != False:
            messages.error(request, verificar.verificacao_geral(
                nome, sobrenome, email=email, senha=senha))
            return redirect('cad_vicediretor')

        try:
            user = User.objects.create_user(
                username=email,
                first_name=nome,
                last_name=sobrenome,
                email=email,
                password=senha
            )
            user.save()
            assign_role(user, 'vicediretor') 
            if form.is_valid():
                vicediretor = form.save()
                vicediretor.user = user
                vicediretor.save()
                messages.success(request, f'{nome} cadastrado com sucesso!')
                return redirect('mostrar_vicediretor')
            else:
                if user:
                    user.delete()
                messages.error(request, 'Formulário inválido!')
                return redirect('cad_vicediretor')
        except:
            if user:
                user.delete()
            messages.error(request, 'Algo deu erro no Cadastro!')
            return redirect('cad_vicediretor')
    return render(request, 'cadastrar_vicediretor.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_coordenador')
def cad_coordenador(request):
    form = CoordenadorModelForm(
                request.POST or None, request.FILES or None)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if verificar.verificacao_geral(nome, sobrenome, email=email, senha=senha) != False:
            messages.error(request, verificar.verificacao_geral(
                nome, sobrenome, email=email, senha=senha))
            return redirect('cad_coordenador')

        try:
            user = User.objects.create_user(
                username=email,
                first_name=nome,
                last_name=sobrenome,
                email=email,
                password=senha
            )
            user.save()
            assign_role(user, 'coordenador')
            if form.is_valid():
                coordenador = form.save()
                coordenador.user = user
                coordenador.save()
                messages.success(request, f'{nome} cadastrado com sucesso!')
                return redirect('mostrar_coordenador')
            else:
                if user:
                    user.delete()
                messages.error(request, 'Formulário inválido!')
                return redirect('cad_coordenador')

        except:
            if user:
                user.delete()
            messages.error(request, 'Algo deu erro no Cadastro!')
            return redirect('cad_coordenador')
    return render(request, 'cadastrar_coordenador.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_secretario')
def cad_secretario(request):
    form = SecretarioModelForm(
                request.POST or None, request.FILES or None)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if verificar.verificacao_geral(nome, sobrenome, email=email, senha=senha) != False:
            messages.error(request, verificar.verificacao_geral(
                nome, sobrenome, email=email, senha=senha))
            return redirect('cad_secretario')

        try:
            user = User.objects.create_user(
                username=email,
                first_name=nome,
                last_name=sobrenome,
                email=email,
                password=senha
            )
            user.save()
            assign_role(user, 'secretario')
            
            if form.is_valid():
                secretario = form.save()
                secretario.user = user
                secretario.save()
                messages.success(request, f'{nome} cadastrado com sucesso!')
                return redirect('mostrar_secretario')
            else:
                if user:
                    user.delete()
                messages.error(request, 'Formulário inválido!')
                return redirect('cad_secretario')
        except:
            if user:
                user.delete()
            messages.error(request, 'Algo deu erro no Cadastro!')
            return redirect('cad_secretario')
    return render(request, 'cadastrar_secretario.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_funcionario')
def cad_funcionario(request):
    form = FuncionarioModelForm(
                request.POST or None, request.FILES or None)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cargo = request.POST.get('cargo')
        if verificar.verificacao_geral(nome, sobrenome, cargo, email=email, senha=senha) != False:
            messages.error(request, verificar.verificacao_geral(
                nome, sobrenome, cargo, email=email, senha=senha))
            return redirect('cad_funcionario')

        try:
            user = User.objects.create_user(
                username=email,
                first_name=nome,
                last_name=sobrenome,
                email=email,
                password=senha
            )
            user.save()
            assign_role(user, 'funcionario')
            
            if form.is_valid():
                funcionario = form.save()
                funcionario.user = user
                funcionario.save()
                messages.success(request, f'{nome} cadastrado com sucesso!')
                return redirect('mostrar_funcionario')
            else:
                if user:
                    user.delete()
                messages.error(request, 'Formulário inválido!')
                return redirect('cad_funcionario')
        except:
            if user:
                user.delete()
            messages.error(request, 'Algo deu erro no Cadastro!')
            return redirect('cad_funcionario')
    return render(request, 'cadastrar_funcionario.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_docente')
def cad_docente(request):
    form = DocenteModelForm(
                request.POST or None, request.FILES or None)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        disciplinas = request.POST.getlist('disciplinas')
        if verificar.verificacao_geral(nome, sobrenome, email=email, senha=senha) != False:
            messages.error(request, verificar.verificacao_geral(
                nome, sobrenome, email=email, senha=senha))
            return redirect('cad_docente')
        try:
            user = User.objects.create_user(
                username=email,
                first_name=nome,
                last_name=sobrenome,
                email=email,
                password=senha
            )
            user.save()
            assign_role(user, 'docente')
            if form.is_valid():
                docente = form.save()
                docente.user = user
                docente.save()
                messages.success(request, f'{nome} cadastrado com sucesso!')
                return redirect('mostrar_docente')
            else:
                if user:
                    user.delete()
                messages.error(request, 'Formulário inválido!')
                return redirect('cad_docente')
        except:
            if user:
                user.delete()
            messages.error(request, 'Algo deu erro no Cadastro!')
            return redirect('cad_docente')
    return render(request, 'cadastrar_docente.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_discente')
def cad_discente(request):
    form = DiscenteModelForm(
                request.POST or None, request.FILES or None)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if verificar.verificacao_geral(nome, sobrenome, email=email, senha=senha) != False:
            messages.error(request, verificar.verificacao_geral(
                nome, sobrenome, email=email, senha=senha))
            return redirect('cad_discente')

        try:
            user = User.objects.create_user(
                username=email,
                first_name=nome,
                last_name=sobrenome,
                email=email,
                password=senha
            )
            user.save()
            assign_role(user,'discente')
            
            if form.is_valid():
                discente = form.save()
                discente.user = user
                discente.save()
                disciplinas = Disciplina.objects.all()
                for disci in disciplinas:
                    notas = NotasDiscentes(
                        disciplina=disci,
                        discente=discente
                    )
                    notas.save()
                messages.success(
                    request, f'{discente.user.first_name} cadastrado com sucesso!')
                return redirect('mostrar_discente')
            else:
                if user:
                    user.delete()
                messages.error(request, 'Formulário inválido!')
                return redirect('cad_discente')
        except:
            if user:
                user.delete()
            messages.error(request, 'Algo deu erro no Cadastro!')
            return redirect('cad_discente')
    return render(request, 'cadastrar_discente.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_turno')
def cad_turno(request):
    form = TurnoModelForm(request.POST or None)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if not nome:
            messages.error(request, 'Nome do turno vazio!')
            return redirect('cad_turno')
        if nome.strip() == '':
            messages.error(request, 'Nome do turno vazio!')
            return redirect('cad_turno')
        if Turno.objects.filter(nome__icontains=nome):
            messages.error(request, 'Turno já existe!')
            return redirect('cad_turno')
        try:
            
            if form.is_valid():
                form.save()
                messages.success(request, f'{nome} cadastrado com sucesso!')
                return redirect('mostrar_turno')
            else:
                messages.error(request, 'Formulário inválido!')
                return redirect('cad_turno')
        except:
            messages.error(request, 'Algo deu erro no Cadastro!')
            return redirect('cad_turno')
    return render(request, 'cadastrar_turno.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_turno')
def cad_turnos_prontos(request):
    turnos = (
        'Matutino',
        'Vespertino',
        'Noturno'
    )
    for turno in turnos:
        if not Turno.objects.filter(nome__icontains=turno).exists():
            Turno.objects.create(
                nome=turno
            ).save()
    messages.success(request, 'Turnos cadastrados com sucesso!')
    return redirect('mostrar_turno')


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_turma')
def cad_turma(request):
    form = TurmaModelForm(request.POST or None)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        turno = request.POST.get('turno')
        if not nome:
            messages.error(request, 'Nome da turma vazio!')
            return redirect('cad_turma')
        if nome.strip() == '':
            messages.error(request, 'Nome da turma vazio!')
            return redirect('cad_turma')
        if Turma.objects.filter(nome=nome,turno=turno):
            messages.error(request, 'Turma já existe nesse turno!')
            return redirect('cad_turma')
        try:
            
            if form.is_valid():
                form.save()
                messages.success(request, f'{nome} cadastrado com sucesso!')
                return redirect('mostrar_turma')
            else:
                messages.error(request, 'Formulário inválido!')
                return redirect('cad_turma')
        except:
            messages.error(request, 'Algo deu erro no Cadastro!')
            return redirect('cad_turma')
    return render(request, 'cadastrar_turma.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_disciplina')
def cad_disciplina(request):
    form = DisciplinaModelForm(request.POST or None)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if not nome:
            messages.error(request, 'Nome da disciplina vazio!')
            return redirect('cad_disciplina')
        if nome.strip() == '':
            messages.error(request, 'Nome da disciplina vazio!')
            return redirect('cad_disciplina')
        if Disciplina.objects.filter(nome=nome):
            messages.error(request, 'Disciplina já existe!')
            return redirect('cad_disciplina')

        try:
            
            if form.is_valid():
                nova_disciplina = form.save()
                discentes = Discente.objects.all()
                for aluno in discentes:
                    NotasDiscentes.objects.create(
                        disciplina=nova_disciplina,
                        discente=aluno
                    ).save()
                messages.success(request, f'{nome} cadastrado com sucesso!')
                return redirect('mostrar_disciplina')
            else:
                messages.error(request, 'Formulário inválido!')
                return redirect('cad_disciplina')
        except:
            messages.error(request, 'Algo deu erro no Cadastro!')
            return redirect('cad_disciplina')
    return render(request, 'cadastrar_disciplina.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator(permission_name='modificar_disciplina')
def cad_dis_prontas(request):
    disciplinas = (
        'Português', 'Matemática',
        'Inglês', 'Geografia', 'Ensino religioso',
        'ICS-Identidade Cultura Significativa',
        'Educação Física', 'Ciências',
        'História', 'Artes')
    for disc in disciplinas:
        if not Disciplina.objects.filter(nome__icontains=disc).exists():
            nova_disciplina = Disciplina.objects.create(
                nome=disc
            )
            nova_disciplina.save()
            discentes = Discente.objects.all()
            for aluno in discentes:
                NotasDiscentes.objects.create(
                    disciplina=nova_disciplina,
                    discente=aluno
                ).save()
    messages.success(request, 'Disciplinas cadastradas com sucesso!')
    return redirect('mostrar_disciplina')

@login_required(login_url='login')
@has_permission_decorator(permission_name='fazer_planejamento_anual')
def cad_planejamento_anual(request):
    form=PlanejamentoAnualModelForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            try:
                docente=get_object_or_404(Docente,user=request.user)
            except:
                messages.error(request,'Você não é docente para cadastrar!')
                return render(request, 'cadastrar_planejamento_anual.html',{'form':form})
            planejamento=form.save()
            planejamento.docente=docente
            planejamento.save()
            messages.success(request,'Plano anual cadastrado com sucesso!')
            return redirect('mostrar_planejamento_anual')
        else:
            messages.error(request,'Formulário não é valido')
            return render(request, 'cadastrar_planejamento_anual.html',{'form':form})
    return render(request, 'cadastrar_planejamento_anual.html',{'form':form})

@login_required(login_url='login')
@has_permission_decorator(permission_name='fazer_plano_de_aula')
def cad_plano_de_aula(request):
    form=PlanoDeAulaModelForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            try:
                docente=get_object_or_404(Docente,user=request.user)
            except:
                messages.error(request,'Você não é docente para cadastrar!')
                return render(request, 'cadastrar_plano_de_aula.html',{'form':form})
            plano=form.save()
            plano.docente=docente
            plano.save()
            messages.success(request,'Plano de aula cadastrado com sucesso!')
            return redirect('mostrar_plano_de_aula')
        else:
            messages.error(request,'Formulário não é valido')
            return render(request, 'cadastrar_plano_de_aula.html',{'form':form})
    return render(request, 'cadastrar_plano_de_aula.html',{'form':form})

@login_required(login_url='login')
@has_permission_decorator(permission_name='fazer_plano_de_curso')
def cad_plano_de_curso(request):
    form=PlanoDeCursoModelForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            try:
                docente=get_object_or_404(Docente,user=request.user)
            except:
                messages.error(request,'Você não é docente para cadastrar!')
                return render(request, 'cadastrar_plano_de_curso.html',{'form':form})
            plano=form.save()
            plano.docente=docente
            plano.save()
            messages.success(request,'Plano de curso cadastrado com sucesso!')
            return redirect('mostrar_plano_de_curso')
        else:
            messages.error(request,'Formulário não é valido')
            return render(request, 'cadastrar_plano_de_curso.html',{'form':form})
    return render(request, 'cadastrar_plano_de_curso.html',{'form':form})