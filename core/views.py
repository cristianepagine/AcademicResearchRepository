from core.models import Registers
from django.shortcuts import redirect
from django.shortcuts import render

#define a pagina index
def index(request):
    return redirect('/register')

# Filtrando os registros por usuário logado na sessão
def list_registers(request):
    usuario = request.user
    if usuario.username == 'admin':
        registers = Registers.objects.all()
    else:
        registers = Registers.objects.filter(user=usuario)
    
    response = {'registers': registers}
    return render(request, 'registers.html', response)
