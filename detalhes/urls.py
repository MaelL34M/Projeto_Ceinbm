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
    path('Diretor/<int:id>',views.detalhes_diretor,name='detalhes_diretor'),
    path('ViceDiretor/<int:id>',views.detalhes_vicediretor,name='detalhes_vicediretor'),
    path('Coordenador/<int:id>',views.detalhes_coordenador,name='detalhes_coordenador'),
    path('Secretario/<int:id>',views.detalhes_secretario,name='detalhes_secretario'),
    path('Funcionario/<int:id>',views.detalhes_funcionario,name='detalhes_funcionario'),
    path('Docente/<int:id>',views.detalhes_docente,name='detalhes_docente'),
    path('Discente/<int:id>',views.detalhes_discente,name='detalhes_discente'),
    path('Turno/<int:id>',views.detalhes_turno,name='detalhes_turno'),
    path('Turma/<int:id>',views.detalhes_turma,name='detalhes_turma'),
    path('Disciplina/<int:id>',views.detalhes_disciplina,name='detalhes_disciplina'),
    path('Planejamento/<int:id>',views.detalhes_planejamento_anual,name='detalhes_planejamento'),
    path('PlanoDeCurso/<int:id>',views.detalhes_plano_de_curso,name='detalhes_plano_de_curso'),
    path('PlanoDeAula/<int:id>',views.detalhes_plano_de_aula,name='detalhes_plano_de_aula'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)