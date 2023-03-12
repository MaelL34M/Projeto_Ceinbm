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
    path('Diretor/<int:id>',views.del_diretor,name='del_diretor'),
    path('ViceDiretor/<int:id>',views.del_vicediretor,name='del_vicediretor'),
    path('Coordenador/<int:id>',views.del_coordenador,name='del_coordenador'),
    path('Secretario/<int:id>',views.del_secretario,name='del_secretario'),
    path('Funcionario/<int:id>',views.del_funcionario,name='del_funcionario'),
    path('Docente/<int:id>',views.del_docente,name='del_docente'),
    path('Discente/<int:id>',views.del_discente,name='del_discente'),
    path('Turno/<int:id>',views.del_turno,name='del_turno'),
    path('Turma/<int:id>',views.del_turma,name='del_turma'),
    path('Disciplina/<int:id>',views.del_disciplina,name='del_disciplina'),
    path('PlanejamentoAnual/<int:id>',views.del_planejamento_anual,name='del_planejamento_anual'),
    path('PlanoDeAula/<int:id>',views.del_plano_de_aula,name='del_plano_de_aula'),
    path('PlanoDeCurso/<int:id>',views.del_plano_de_curso,name='del_plano_de_curso'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)