from django.shortcuts import render
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