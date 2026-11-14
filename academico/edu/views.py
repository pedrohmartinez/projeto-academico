from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Matricula

# Create your views here.

def index(request):
    
    matriculas = Matricula.objects.all()
    
    dados = {
        'matriculas' : matriculas,
    }
    
    return render(request, 'index.html', dados)

def cadastro(request):
    return render(request, 'cadastro.html')

def edu(request, matricula_id):
    matricula = get_object_or_404(Matricula, pk=matricula_id)
    
    matricula_a_exibir = {
        'matricula': matricula
    }
    
    return render(request, 'matricula.html', matricula_a_exibir)