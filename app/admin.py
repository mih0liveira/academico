from django.contrib import admin
from .models import *

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]


class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoInline]


class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline]


class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]



class AlunoTurmaInline(admin.TabularInline):
    model = AlunoTurma
    extra = 1

class TurmaAdmin(admin.ModelAdmin):
    inlines = [AlunoTurmaInline]


class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'uf']
    list_filter = ['uf']
    search_fields = ['nome']

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class PessoaAdmin(admin.ModelAdmin):
    inlines = [FrequenciaInline]
    list_display = ['nome', 'cpf', 'email']
    search_fields = ['nome', 'cpf']


admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(InstituicaoEnsino, InstituicaoEnsinoAdmin)
admin.site.register(AreaSaber, AreaSaberAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(AvaliacaoTipo)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Turno)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)
admin.site.register(AlunoTurma) 