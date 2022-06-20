from ast import pattern
from django.urls import path
from .views import index,regUsuario,recContra,inicio,perfil,apirest,paginaAyuda,ayuda,chat

urlpatterns = [
    path('',index,name="index"),
    path('registro-usuario/',regUsuario,name="registroUsuario"),
    path('recuperar-contraseña/',recContra,name="recuperarContrasena"),
    path('inicio/', inicio,name="inicio"),
    path('perfil/',perfil,name="perfil"),
    path('precioRp/',apirest, name="api"),
    path('ayuda/',paginaAyuda, name="ayuda"),
    path('ayuda2/', ayuda, name="ayuda2"),
    path('chat/',chat,name="chat")
    
]