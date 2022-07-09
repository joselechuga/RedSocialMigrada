from django.shortcuts import render
from .models import usuarios,Message,Room
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
from rest_framework import viewsets
from .serializers import UsuariosSerializers

# Create your views here.

class usuarioViewset(viewsets.ModelViewSet):
    queryset = usuarios.objects.all()
    serializer_class = UsuariosSerializers



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

def games(request):
    return render(request,'core/recomendados/games.html')

def paginaAyuda(request):
    return render(request,'core/ayuda/ayuda.html')

def ayuda(request):
    return render(request,'core/ayuda/ayuda2.html')

def ayuda3(request):
    return render(request,'core/ayuda/ayuda3.html')

def chat(request):
    return render(request,'core/Mensajeria/chat.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'core/Mensajeria/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


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


