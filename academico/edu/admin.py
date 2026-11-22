from django.contrib import admin
from .models import Matricula, Curso

# Register your models here.

class AdminMatricula(admin.ModelAdmin):
    
    list_display = ( 'id', 'matricula', 'aluno', 'curso')
    list_display_links = ('id', 'aluno', 'curso')
    search_fields = ('aluno__user__username', 'matricula')
    list_filter = ('curso', )
    list_per_page = (10)
    
class AdminCursos(admin.ModelAdmin):
    
    list_display = ('id', 'descricao', 'codigo', 'ativo')
    list_display_links = ('id', 'descricao', 'codigo')
    list_editable = ('ativo',)
    search_fields = ('descricao', 'codigo')
    readonly_fields = ('codigo',)
    list_per_page = 10
    
admin.site.register(Matricula, AdminMatricula)
admin.site.register(Curso, AdminCursos)