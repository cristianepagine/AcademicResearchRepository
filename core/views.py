from django.contrib import messages
from core.models import Registers
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout


#define a pagina index
#def index(request):
 #   return redirect('/register')
 
 
#função que renderiza a pagina de login
def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

#função que efetuaa login
def submit_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou Senha Inválidos")
    return redirect('/')

# Filtrando os registros por usuário logado na sessão
@login_required(login_url='/login/')
def list_registers(request):
    usuario = request.user
    if usuario.username == 'admin':
        registers = Registers.objects.all()
    else:
        registers = Registers.objects.filter(user=usuario)
    
    response = {'registers': registers}
    return render(request, 'registers.html', response)

@login_required(login_url='/login/')
def fichamento(request):
    return render(request, 'fichamento.html')