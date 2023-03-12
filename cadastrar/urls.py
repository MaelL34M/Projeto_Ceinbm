from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404,handler403
from principal.views import erro403,erro404

handler404=erro404
handler403= erro403
urlpatterns = [
    path('Diretor/',views.cad_diretor,name='cad_diretor'),
    path('ViceDiretor/',views.cad_vicediretor,name='cad_vicediretor'),
    path('Coordenador/',views.cad_coordenador,name='cad_coordenador'),
    path('Secretario/',views.cad_secretario,name='cad_secretario'),
    path('Funcionario/',views.cad_funcionario,name='cad_funcionario'),
    path('Docente/',views.cad_docente,name='cad_docente'),
    path('Discente/',views.cad_discente,name='cad_discente'),
    path('Turno/',views.cad_turno,name='cad_turno'),
    path('TurnosProntos/',views.cad_turnos_prontos,name='cad_turnos_prontos'),
    path('Turma/',views.cad_turma,name='cad_turma'),
    path('Disciplina/',views.cad_disciplina,name='cad_disciplina'),
    path('DisciplinaProntas/',views.cad_dis_prontas,name='cad_dis_prontas'),
    path('Planejamento/',views.cad_planejamento_anual,name='cad_planejamento_anual'),
    path('PlanoDeAula/',views.cad_plano_de_aula,name='cad_plano_de_aula'),
    path('PlanoDeCurso/',views.cad_plano_de_curso,name='cad_plano_de_curso'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)