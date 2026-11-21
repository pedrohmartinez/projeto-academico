from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')

        if not nome or not email or not senha or not senha2:
            print('Preencha todos os campos')
            return redirect('cadastro')

        if senha != senha2:
            print('As senhas não conferem')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            print('E-mail já cadastrado')
            return redirect('cadastro')

        if User.objects.filter(username=nome).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('Cadastro realizado com sucesso!')
        return redirect('login')

    return render(request, 'comum/cadastro.html')

def dashboard(request):
    return render(request, 'comum/dashboard.html')

def login(request):
    if request.method == 'POST':
            email = request.POST["email"]
            senha = request.POST["senha"]
            
            if User.objects.filter(email=email).exists():
                nome = User.objects.filter(email=email).values_list('username', flat=True).get()
                user = auth.authenticate(request, username=nome, password=senha)
                
                if user is not None:
                    auth.login(request, user)
                    print('Login realizado com sucesso!')
                    return redirect('dashboard')
                else:
                    print('Falha na autentificação')
                    return redirect('login')
            else:
                print('E-mail não cadastado')
                return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        
        else:
            return render(request, 'comum/login.html')

def logout(request):    
    auth.logout(request)
    return redirect('index')