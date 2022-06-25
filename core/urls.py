from importlib.resources import path
from django import views
from django.urls import URLPattern, path
from django.contrib.auth.views import LoginView,LogoutView
from . import views
from .views import index,regUsuario,recContra,inicio,perfil,apirest,paginaAyuda,ayuda,chat,listaSeguidores,log,register

urlpatterns = [
    path('',index,name="index"),
    path('recuperar-contraseña/',recContra,name="recuperarContrasena"),
    path('inicio/', inicio,name="inicio"),
    path('perfil/',perfil,name="perfil"),
    path('precioRp/',apirest, name="api"),
    path('ayuda/',paginaAyuda, name="ayuda"),
    path('ayuda2/', ayuda, name="ayuda2"),
    path('chat/',chat,name="chat"),
    path('lista-seguidores/',listaSeguidores,name="listaSeguidores"),
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='core/Registro_usuario/login.html'),name='login'),
    
]