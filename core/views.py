from django.shortcuts import render
from .models import usuarios
from contextvars import Context
from email import message
from multiprocessing import context
from telnetlib import AUTHENTICATION
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import  UserRegisterForm
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'core/index.html')

def regUsuario(request):
    return render(request,'core/Registro_usuario/registroUsuario.html')

def recContra(request):
    return render(request,'core/Registro_usuario/recuperarContrasena.html')

def inicio(request):
    return render(request,'core/inicio/inicio.html')

def perfil(request):
    return render(request,'core/perfil/perfil.html')

def apirest(request):
    return render(request,'core/apirest/api.html')

def paginaAyuda(request):
    return render(request,'core/ayuda/ayuda.html')

def ayuda(request):
    return render(request,'core/ayuda/ayuda2.html')

def ayuda3(request):
    return render(request,'core/ayuda/ayuda3.html')

def chat(request):
    return render(request,'core/Mensajeria/chat.html')

def listaSeguidores(request):

    usuario = usuarios.objects.all()

    datos = {
        "usuarios":usuario
    }

    return render(request,'core/perfil/listaSeguidores.html',datos)

def borrarUsuario(reques,id):

    usuario = usuarios.objects.get(usuario=id)
    usuario.delete()
    return redirect(to='listaSeguidores')


#REGISTRO Y LOGIN  
def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('index')
    else:
        form=UserRegisterForm()
    
    context = { 'form' : form}
    return render(request,'core/Registro_usuario/register.html', context) 

def log(request):
    return render(request,'core/Registro_usuario/login.html')