from django.shortcuts import render, redirect
from .models import usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        novo_usuario = usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()

        # Limpar os campos do formulário após o envio
        nome = ''
        idade = ''

        # Redirecionar após o envio do formulário
        return redirect('listagem_usuarios')

    usuarios = {
        'usuarios': usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)
