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
    path('Diretor/<int:id>',views.edt_diretor,name='edt_diretor'),
    path('ViceDiretor/<int:id>',views.edt_vicediretor,name='edt_vicediretor'),
    path('Coordenador/<int:id>',views.edt_coordenador,name='edt_coordenador'),
    path('Secretario/<int:id>',views.edt_secretario,name='edt_secretario'),
    path('Funcionario/<int:id>',views.edt_funcionario,name='edt_funcionario'),
    path('Docente/<int:id>',views.edt_docente,name='edt_docente'),
    path('Discente/<int:id>',views.edt_discente,name='edt_discente'),
    path('Turno/<int:id>',views.edt_turno,name='edt_turno'),
    path('Turma/<int:id>',views.edt_turma,name='edt_turma'),
    path('Disciplina/<int:id>',views.edt_disciplina,name='edt_disciplina'),
    path('Planejamento/<int:id>',views.edt_planejamento_anual,name='edt_planejamento'),
    path('PlanoDeAula/<int:id>',views.edt_plano_de_aula,name='edt_plano_de_aula'),
    path('PlanoDeCurso/<int:id>',views.edt_plano_de_curso,name='edt_plano_de_curso'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)