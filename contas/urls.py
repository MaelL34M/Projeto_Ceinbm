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
    path('',views.logar,name='login'),
    path('sair/',views.sair,name='sair'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)