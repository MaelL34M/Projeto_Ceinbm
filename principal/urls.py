from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404,handler403

handler404=views.erro404
handler403= views.erro403
urlpatterns = [
    path('',views.home,name='home'),
    path('cadastrar/',include('cadastrar.urls')),
    path('editar/',include('editar.urls')),
    path('detalhes/',include('detalhes.urls')),
    path('apagar/',include('apagar.urls')),


    path('Diretores/',views.mostrar_diretor,name='mostrar_diretor'),
    path('Vice-diretores/',views.mostrar_vicediretor,name='mostrar_vicediretor'),
    path('Coordenadores/',views.mostrar_coordenador,name='mostrar_coordenador'),
    path('Secretarios/',views.mostrar_secretario,name='mostrar_secretario'),
    path('Funcionarios/',views.mostrar_funcionario,name='mostrar_funcionario'),
    path('Docentes/',views.mostrar_docente,name='mostrar_docente'),
    path('Discentes/',views.mostrar_discente,name='mostrar_discente'),
    path('Turnos/',views.mostrar_turno,name='mostrar_turno'),
    path('Turmas/',views.mostrar_turma,name='mostrar_turma'),
    path('Disciplinas/',views.mostrar_disciplina,name='mostrar_disciplina'),
    path('PlanejamentosAnuais/',views.mostrar_planejamento_anual,name='mostrar_planejamento_anual'),
    path('PlanosDeAulas/',views.mostrar_planos_de_aulas,name='mostrar_plano_de_aula'),
    path('PlanosDeCursos/',views.mostrar_planos_de_cursos,name='mostrar_plano_de_curso'),


    path('EditarNota/<int:id_disciplina>/<int:id_discente>',views.edt_nota_discente,name='edt_nota_discente'),
    path('detalhesNotas/',views.mostrar_notas,name='mostrar_notas'),

    path('chamada_turmas/<int:id_turma>/',views.fazer_chamada,name='fazer_chamada'),
    path('turmas_chamadas/<int:id_turma>/',views.mostrar_chamadas,name='mostrar_chamadas'),
    path('detalhes_chamada/<int:id_chamada>/',views.detalhes_chamada,name='detalhes_chamada'),

    path('situacao_discente/<int:id_discente>/',views.situacao_discente,name='situacao_discente'),
    path('situacao_discentes/<int:id_turma>/',views.situacao_discentes,name='situacao_discentes'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)