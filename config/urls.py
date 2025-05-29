"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('curso/', CursosView.as_view(), name='curso'),
    path('ocupacao/', OcupacoesView.as_view(), name='ocupacao'),
    path('disciplina/', DisciplinasView.as_view(), name='disciplina'),
    path('pessoa/', PessoasView.as_view(), name='pessoa'),
    path('instituicao/', InstituicoesView.as_view(), name='instituicao'),
    path('avaliacao/', AvaliacoesView.as_view(), name='avaliacao'),
    path('frequencia/', FrequenciasView.as_view(), name='frequencia'),
    path('area_saber/', AreasSaberView.as_view(), name='area_saber'),
    path('turma/', TurmasView.as_view(), name='turma'),
    path('matricula/', MatriculasView.as_view(), name='matricula'),
     path('turno/', TurnosView.as_view(), name='turno'),
    path('cidade/', CidadesView.as_view(), name='cidade'),
    path('ocorrencia/', OcorrenciasView.as_view(), name='ocorrencia'),
    path('avaliacao_tipo/', AvaliacaoTiposView.as_view(), name='avaliacao_tipo'),
    path('curso_disciplina/', CursosDisciplinasView.as_view(), name='curso_disciplina'),
]
