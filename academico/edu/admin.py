from django.contrib import admin
from .models import Matricula

# Register your models here.

class AdminMatricula(admin.ModelAdmin):
    list_display = ( 'id', 'matricula', 'nome_aluno')
    list_display_links = ('id', 'nome_aluno')
    search_fields = ('nome_aluno', )
    list_filter = ('curso', )
    list_per_page = (2)
admin.site.register(Matricula, AdminMatricula)