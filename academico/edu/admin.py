from django.contrib import admin
from .models import Matricula

# Register your models here.

class AdminMatricula(admin.ModelAdmin):
    list_display = ( 'id', 'matricula', 'aluno')
    list_display_links = ('id', 'aluno')
    search_fields = ('aluno__user__first_name', )
    list_filter = ('curso', )
    list_per_page = (2)
admin.site.register(Matricula, AdminMatricula)