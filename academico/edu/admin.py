from django.contrib import admin
from .models import Matricula

# Register your models here.

class AdminMatricula(admin.ModelAdmin):
    list_display = ( 'id', 'matricula', 'aluno')
    list_display_links = ('id', 'aluno', 'curso')
    search_fields = ('aluno__user__username', 'matricula')
    list_filter = ('curso', )
    list_per_page = (10)
    
    
admin.site.register(Matricula, AdminMatricula)