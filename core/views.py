from django.shortcuts import render


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

def chat(request):
    return render(request,'core/Mensajeria/chat.html')