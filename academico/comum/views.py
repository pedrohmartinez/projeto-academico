from django.shortcuts import render

# Create your views here.

def cadastro(request):
    return render(request, 'comum/cadastro.html')

def dashboard(request):
    return render(request, 'comum/dashboard.html')

def login(request):
    return render(request, 'comum/login.html')

def logout(request):    
    pass