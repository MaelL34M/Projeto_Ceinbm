from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.validators import validate_email
def verificacao_geral(*args,email,senha):
    for arg in args:
        if not arg:
            return 'Não pode ter campos vazios!'
        if arg.strip()=='':
            return 'Não pode ter campos vazios!'
    if len(senha)<8:
        return 'Senha menor que 8 caracteres!'
    if senha.isnumeric():
        return 'Senha não pode ser totalmente numérica!'
    if senha.isalpha():
        return 'Senha deve conter números!'
    if User.objects.filter(email=email):
        return 'Email já cadastrado!'
    try:
        validate_email(email)
    except:
        return 'Esse email não é válido'
    return False

def verificacao_geral_editar(*args):

    for arg in args:
        if not arg:
            return 'Não pode ter campos vazios!'
        if arg.strip()=='':
            return 'Não pode ter campos vazios!'
    return False
def verificar_campos_vazios(nome,sobrenome,email,senha):
    if not nome or not sobrenome or not email or not senha:
        return 'Não pode ter campos vazios!'
    return False

def verificar_senha(senha):
    if len(senha)<8:
        return 'Senha menor que 8 caracteres!'
    if senha.isnumeric():
        return 'Senha não pode ser totalmente numérica!'
    if senha.isalpha():
        return 'Senha deve conter números!'
    return False