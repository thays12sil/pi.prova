"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from curso import views
from django.conf import settings
from django.conf.urls.static import static
from gerencia.views import index, editar_categoria, excluir
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index' ), # index
    path('usuario/',include('usuarios.urls')),
    path('gerencia/',include('gerencia.urls')),
    path('curso/<int:curso_id>',views.detalhe_curso,name='detalhe_curso'),
    path('sobre/',views.pagina_sobre,name='pagina_sobre'),
    path('teste/',views.pagina_teste,name='pagina_teste'),
    path('categoria/editar/<int:id>', editar_categoria, name='editar_categoria'),
    path('categoria/editar/excluir/<int:id>', excluir, name='excluir'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
