from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from django.core.validators import validate_email
# Create your views here.
def logar(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        email=request.POST.get('email')
        senha= request.POST.get('senha')
        try:
            validate_email(email)
        except:
            messages.error(request, 'Email não é válido')
            return redirect('/')
        usuario = authenticate(username=email,password=senha)
        if not usuario:
            messages.error(request, 'Email e senha incorretos.')
            return redirect('/')
        else:
            login(request, usuario)
            return redirect('home')
    return render(request,'login.html')

def sair(request):
    logout(request)
    return redirect('/')
