from django.contrib import admin
from .models import Diretor,ViceDiretor,Coordenador,Secretario,Funcionario,Docente,Discente,Disciplina,Turma,NotasDiscentes,Chamada,Chamada_Discentes
# Register your models here.
admin.site.register(Diretor)
admin.site.register(ViceDiretor)
admin.site.register(Coordenador)
admin.site.register(Secretario)
admin.site.register(Funcionario)
admin.site.register(Docente)
admin.site.register(Discente)
admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(NotasDiscentes)
admin.site.register(Chamada)
admin.site.register(Chamada_Discentes)