from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.messages import constants
from django.contrib import messages
import re
from django.core.exceptions import ValidationError

# Create your views here.
def validacao_cadastro_usuario_exists(request, usuario, email):
    if CustomUser.objects.filter(username=usuario).exists():
        messages.add_message(request, constants.ERROR, 'Já existe um cadastro com este Usuário!')
        return True
    
    if CustomUser.objects.filter(email=email).exists():
        messages.add_message(request, constants.ERROR, 'Já existe um cadastro com este Email!')
        return True
    
    return False


def validacao_cadastro_usuario(request, nome_completo, email, whatsapp, usuario, senha):
    whatsapp = str(whatsapp)
    regex_nome_completo = r'^[a-zA-ZáéíóúâêôãçÁÉÍÓÚÂÊÔÃÇ ]{7,100}$'
    regex_whatsapp = r'^(?:[(]\d{2}[)] \d{1} \d{4}-\d{4})$'
    regex_email = r'^[a-zA-Z0-9\-_]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9]+$'
    regex_usuario = r'^[a-zA-Z0-9_\-@]{4,150}$'
    regex_senha = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\-_@#$&])[A-Za-z0-9\-_@#$&]{8,25}$'

  
    if not re.match(regex_nome_completo, nome_completo):
        messages.add_message(request, constants.ERROR, 'O campo Nome Completo está preenchido incorretamente, tente novamente!')
        return False

    if not re.match(regex_email, email) or len(email.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'O campo E-mail está preenchido incorretamente, tente novamente!')
        return False

    if not re.match(regex_whatsapp, whatsapp) or len(whatsapp.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'O campo Whatsapp está preenchido incorretamente, tente novamente!')
        return False

    if not re.match(regex_usuario, usuario) or len(usuario.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'O campo Usuário está preenchido incorretamente, tente novamente!')
        return False

    if not re.match(regex_senha, senha) or len(senha.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'O campo Senha está preenchido incorretamente, tente novamente!')
        return False

    return True

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    elif request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        email = request.POST.get('email')
        whatsapp = request.POST.get('whatsapp')
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        dados_submetidos =  {
            'nome_completo': nome_completo,
            'email': email,
            'whatsapp': whatsapp,
            'usuario': usuario,
            'senha': senha,
            'confirmar_senha': confirmar_senha

        }

        if not validacao_cadastro_usuario(request, nome_completo, email, whatsapp, usuario, senha):
            return render(request, 'cadastro.html', {'dados_submetidos': dados_submetidos})
                
        if validacao_cadastro_usuario_exists(request, usuario, email):
            return render(request, 'cadastro.html', {'dados_submetidos': dados_submetidos})

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'A senha e confirmar senha não são iguais!')
            return render(request, 'cadastro.html', {'dados_submetidos': dados_submetidos})

        try:
            user = CustomUser.objects.create_user(
                first_name=nome_completo,
                email=email,
                whatsapp=whatsapp,
                username=usuario,
                password=senha,

            )

            user.save()

            messages.add_message(request, constants.SUCCESS, 'Usuário Cadastrado com Sucesso!')
            return redirect('home')

        except ValidationError as e:
            messages.add_message(request, ConnectionResetError, f'{e} - Erro ao Cadatrar Usuário!')
            return render(request, 'cadastro.html', {'dados_submetidos': dados_submetidos})

