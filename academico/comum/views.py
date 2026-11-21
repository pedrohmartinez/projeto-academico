from django.shortcuts import render, redirect
# Create your views here.

def cadastro(request):
    return render(request, 'comum/cadastro.html')

def dashboard(request):
    return render(request, 'comum/dashboard.html')

def login(request):
    if request.method == 'POST':
            print('REQUISIÇÃO POST')
            return redirect('index')
    else:
        return render(request, 'comum/login.html')

def logout(request):    
    pass