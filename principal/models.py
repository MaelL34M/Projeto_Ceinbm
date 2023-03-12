from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Usuario(models.Model):
    texto_ajuda_senha = 'A senha deverá ter no mínimo 8 caracteres. Deverá ter números e letras.'
    generos = [
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Outro', 'Outro')
    ]
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    genero = models.CharField(
        max_length=30, choices=generos, verbose_name='Gênero', default='Outro')
    email = models.EmailField()
    senha = models.CharField(max_length=128, help_text=texto_ajuda_senha)
    cpf = models.CharField(max_length=14, blank=True, verbose_name='CPF')
    rg = models.CharField(max_length=13, blank=True, verbose_name='RG')
    data_de_nascimento = models.DateField(
        blank=True, null=True, default='01/01/2000', verbose_name='Data de Nascimento')

    class Meta:
        abstract = True


class Diretor(Usuario):
    cargo = models.CharField(
        max_length=100, default='Diretor', verbose_name='Cargo')
    foto = models.ImageField(upload_to='fotos_diretores/',
                             blank=True, null=True, verbose_name='Foto')

    def __str__(self):
        return super().user.first_name

    def delete(self, *args, **kwargs):
        self.foto.delete()
        self.user.delete()
        super().delete(*args, **kwargs)


class ViceDiretor(Usuario):
    cargo = models.CharField(
        max_length=100, default='Vice-diretor', verbose_name='Cargo')
    foto = models.ImageField(
        upload_to='fotos_vice-diretores/', blank=True, null=True, verbose_name='Foto')

    def __str__(self):
        return super().user.first_name

    def delete(self, *args, **kwargs):
        self.foto.delete()
        self.user.delete()
        super().delete(*args, **kwargs)


class Coordenador(Usuario):
    cargo = models.CharField(
        max_length=100, default='Coordenador', verbose_name='Cargo')
    foto = models.ImageField(
        upload_to='fotos_coordenadores/', blank=True, null=True, verbose_name='Foto')

    def __str__(self):
        return super().user.first_name

    def delete(self, *args, **kwargs):
        self.foto.delete()
        self.user.delete()
        super().delete(*args, **kwargs)


class Secretario(Usuario):
    cargo = models.CharField(
        max_length=100, default='Secretário', verbose_name='Cargo')
    foto = models.ImageField(
        upload_to='fotos_secretarios/', blank=True, null=True, verbose_name='Foto')

    def __str__(self):
        return super().user.first_name

    def delete(self, *args, **kwargs):
        self.foto.delete()
        self.user.delete()
        super().delete(*args, **kwargs)


class Funcionario(Usuario):
    cargo = models.CharField(max_length=100, verbose_name='Cargo')
    foto = models.ImageField(
        upload_to='fotos_funcionarios/', blank=True, verbose_name='Foto')

    def __str__(self):
        return super().user.first_name

    def delete(self, *args, **kwargs):
        self.foto.delete()
        self.user.delete()
        super().delete(*args, **kwargs)


class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Disciplina')
    carga_horaria = models.IntegerField(
        null=True, verbose_name='Carga Horária em horas')

    def __str__(self):
        return self.nome


class Turno(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome da Turma')
    turno = models.ForeignKey(
        Turno, on_delete=models.SET_NULL,null=True, related_name='turmas')

    def __str__(self):
        return f'{self.nome}-{self.turno.nome}'


class Discente(Usuario):
    situacoes = [
        ('Em andamento', 'Em andamento'),
        ('Aprovado', 'Aprovado'),
        ('Reprovado', 'Reprovado'),
        ('Reprovado por falta', 'Reprovado por falta'),
        ('Prova Final', 'Prova Final'),
        ('Aprovado pelo Conselho', 'Aprovado pelo Conselho'),
        ('Reprovado pelo Conselho', 'Reprovado pelo Conselho')]
    foto = models.ImageField(
        upload_to='fotos_dos_discentes/', blank=True, verbose_name='Foto')
    nome_responsavel = models.CharField(
        max_length=250, blank=True, verbose_name='Nome do responsável')
    segundo_responsavel = models.CharField(
        max_length=250, blank=True, verbose_name='Nome do segundo responsável')
    telefone1 = models.CharField(
        max_length=20, blank=True, verbose_name='Telefone do responsável')
    telefone2 = models.CharField(
        max_length=20, blank=True, verbose_name='Telefone do segundo responsável')
    endereco = models.CharField(
        max_length=250, blank=True, verbose_name='Endereço do aluno')
    nis = models.CharField(max_length=15, blank=True,
                           verbose_name='NIS do aluno')
    situacao = models.CharField(
        max_length=25, choices=situacoes, default='Em andamento')

    pais_separados = models.BooleanField(
        default=False, verbose_name='Pais separados?')
    pcd = models.BooleanField(
        default=False, verbose_name='Possui deficiência?')
    pcd_detalhes = models.TextField(
        blank=True, verbose_name='Detalhes da deficiência')
    rest_alimentar = models.BooleanField(
        default=False, verbose_name='Possui restrição alimentar?')
    rest_alimentar_detalhes = models.TextField(
        blank=True, verbose_name='Detalhes da restrição alimentar')
    usa_medicamentos = models.BooleanField(
        default=False, verbose_name='Usa medicamentos?')
    usa_medicamentos_detalhes = models.TextField(
        blank=True, verbose_name='Detalhes dos medicamentos')

    obs = models.TextField(blank=True, verbose_name='Observações do aluno')
    turma = models.ManyToManyField(Turma,blank=True, verbose_name='Turma do aluno', related_name='alunos')
    disciplinas = models.ManyToManyField(
        Disciplina, related_name='disciplinas', through='NotasDiscentes')
    cargo = models.CharField(
        max_length=100, default='Discente', verbose_name='Cargo')

    def __str__(self):
        return super().user.first_name

    def delete(self, *args, **kwargs):
        self.foto.delete()
        self.user.delete()
        super().delete(*args, **kwargs)


class NotasDiscentes(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE,
                                   verbose_name='Nome da disciplina', related_name='notas_discentes')
    discente = models.ForeignKey(Discente, on_delete=models.CASCADE,
                                 verbose_name='Nome do Discente', related_name='notas_discentes')
    situacoes = [
        ('Em andamento', 'Em andamento'),
        ('Aprovado', 'Aprovado'),
        ('Reprovado', 'Reprovado'),
        ('Reprovado por falta', 'Reprovado por falta'),
        ('Prova Final', 'Prova Final')]
    faltas = models.IntegerField(default=0, verbose_name='Número de faltas')
    nota1 = models.FloatField(default=0, verbose_name='Primeira nota')
    nota2 = models.FloatField(default=0, verbose_name='Segunda nota')
    nota3 = models.FloatField(default=0, verbose_name='Terceira nota')
    media = models.FloatField(default=0, verbose_name='Médias das notas')
    situacao = models.CharField(max_length=50, choices=situacoes,
                                default='Em andamento', verbose_name='Situação do aluno')
    nota_pf=models.FloatField(default=0,blank=True,verbose_name='Nota da Prova Final')
    obs = models.TextField(blank=True, verbose_name='Observações do aluno')

    def __str__(self):
        return f'{self.discente.user.first_name} {self.disciplina.nome}'


class Chamada(models.Model):
    turma = models.ForeignKey(
        Turma, on_delete=models.CASCADE, related_name='chamadas')
    disciplina = models.ForeignKey(
        Disciplina, on_delete=models.CASCADE, related_name='chamadas')
    data_da_chamada = models.DateField(
        auto_now_add=True, verbose_name='Data da chamada')

    def __str__(self):
        return f'{self.data_da_chamada} {self.turma.nome} {self.disciplina.nome}'
    
class Chamada_Discentes(models.Model):
    discente = models.ForeignKey(
        Discente, on_delete=models.CASCADE, related_name='chamada_discentes')
    quant_faltas = models.IntegerField(default=0)
    chamada=models.ForeignKey(Chamada,on_delete=models.CASCADE,verbose_name='Chamada',related_name='chamadas_discentes')

class Docente(Usuario):
    cargo = models.CharField(
        max_length=100, default='Docente', verbose_name='Cargo')
    foto = models.ImageField(upload_to='fotos_docentes/',
                             blank=True, verbose_name='Foto')
    disciplinas = models.ManyToManyField(
        Disciplina, blank=True, verbose_name='Disciplinas que trabalha', related_name='docentes')

    def __str__(self):
        return super().user.first_name

    def delete(self, *args, **kwargs):
        self.foto.delete()
        self.user.delete()
        super().delete(*args, **kwargs)

class Documentos(models.Model):
    documentos = models.FileField(
        upload_to='documentos/', blank=True, verbose_name='Documentos enviados')
    docente=models.ForeignKey(Docente,on_delete=models.SET_NULL,null=True,related_name='documentos')

class PlanejamentoAnual(models.Model):
    trimestres=[
        ('I Trimestre','I Trimestre'),
        ('II Trimestre','II Trimestre'),
        ('III Trimestre','III Trimestre'),
    ]
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE,verbose_name='Docente', related_name='planejamentos',blank=True,null=True)
    disciplina= models.ForeignKey(Disciplina,on_delete=models.CASCADE,verbose_name='Componente curricular',related_name='planejamento_anual')
    data_do_planejamento = models.DateField(auto_now_add=True, verbose_name='Data do Planejamento')
    trimestre= models.CharField(max_length=20, choices=trimestres,verbose_name='Trimestre')
    unidades_tematicas=models.TextField(blank=True,verbose_name='Unidades Temáticas')
    habilidades=models.TextField(blank=True,verbose_name='Habilidades')
    objetos_de_conhecimento=models.TextField(blank=True,verbose_name='Objetos de conhecimento')
    orientações_didaticas=models.TextField(blank=True,verbose_name='Orientações didáticas')
    avaliacao=models.TextField(blank=True,verbose_name='Avaliação')
    fonte=models.TextField(blank=True,verbose_name='Fonte')

    def __str__(self):
        return f'{self.data_do_planejamento}-{self.docente.nome}-{self.disciplina.nome}-{self.trimestre}'

class PlanoDeCurso(models.Model):
    trimestres=[
        ('I Trimestre','I Trimestre'),
        ('II Trimestre','II Trimestre'),
        ('III Trimestre','III Trimestre'),
    ]
    docente=models.ForeignKey(Docente,on_delete=models.SET_NULL,null=True,blank=True)
    disciplina=models.ForeignKey(Disciplina,on_delete=models.CASCADE,verbose_name='Componente curricular',related_name='plano_curso')
    data_do_planejamento = models.DateField(auto_now_add=True, verbose_name='Data do Plano de curso')
    area_do_conhecimento=models.CharField(max_length=25,verbose_name='Área do conhecimento')
    trimestre= models.CharField(max_length=20, choices=trimestres,verbose_name='Trimestre')
    campo_de_atuacao=models.TextField(blank=True,verbose_name='Campo de atução - Unidade temática')
    objetos_do_conhecimento=models.TextField(blank=True,verbose_name='Objetos do conhecimento')
    compentecias=models.TextField(blank=True,verbose_name='Competências')
    habilidades=models.TextField(blank=True,verbose_name='Habilidades')
    avaliação=models.TextField(blank=True,verbose_name='Avaliação')
    def __str__(self):
        return f'{self.data_do_planejamento}-{self.disciplina.nome}-{self.trimestre}'

class PlanoDeAula(models.Model):
    intervencoes=[
        (None,'Outros'),
        ('Recuperação paralela','Recuperação paralela'),
        ('Acompanhamento individual','Acompanhamento individual'),
        ('Mudança na metodologia','Mudança na metodologia'),
        ('Revisão','Revisão'),
        ('Correção oral','Correção oral'),
        ('Aplicação de outra atividade que contemple a mesma habilidade','Aplicação de outra atividade que contemple a mesma habilidade'),
    ]
    docente=models.ForeignKey(Docente,on_delete=models.CASCADE,verbose_name='Docente',related_name='plano_aula',blank=True,null=True)
    turma=models.ForeignKey(Turma,on_delete=models.CASCADE,verbose_name='Ano - Série',related_name='plano_aula')
    disciplina=models.ForeignKey(Disciplina,on_delete=models.CASCADE,verbose_name='Componente Curricular',related_name='plano_aula')
    data=models.DateField(verbose_name='Data',help_text='Formato: 01/01/2000')
    quant_aulas=models.IntegerField(verbose_name='Quantidade de aulas')
    area_do_conhecimento=models.TextField(blank=True,verbose_name='Área do Conhecimento')
    objetos_conhecimento=models.TextField(blank=True,verbose_name='Objetos do Conhecimento')
    compentecias=models.TextField(blank=True,verbose_name='Competências')
    habilidades=models.TextField(blank=True,verbose_name='Habilidades a serem desenvolvidas')
    estrategias=models.TextField(blank=True,verbose_name='Estratégias e ações - Práticas pedagógicas',help_text='Lembrete: (Como a aula será direciona, metodologia a ser implantada).')
    intervencao=models.CharField(max_length=650,choices=intervencoes,verbose_name='Intervenção Pedagógica')
    intervencao_outros=models.TextField(verbose_name='Intervenção Pedagógica',help_text='Caso houver outras interveções')
    materiais=models.TextField(blank=True,verbose_name='Materiais, tecnologia e recursos utilizados:')
    avaliacao=models.TextField(blank=True,verbose_name='Avaliação',help_text='Lembrete: Avaliação diagnóstica e formativa por meio de exercício diagnóstico e apresentação de trabalho oral, mediante a temática proposta da aula.')
    def __str__(self):
        return f'{self.docente.nome}-{self.disciplina.nome}-{self.turma.nome}'