from importlib.resources import path
from xml.etree.ElementInclude import include
from django import views
from django.db import router
from django.urls import URLPattern, path,include
from django.contrib.auth.views import LoginView,LogoutView
from . import views
from .views import index,regUsuario,recContra,inicio,perfil,apirest,paginaAyuda,ayuda,ayuda3,chat,room,listaSeguidores,borrarUsuario,log,register, usuarioViewset,games
from rest_framework import routers
#API
router = routers.DefaultRouter()
router.register('usuario',usuarioViewset)

urlpatterns = [
    path('',index,name="index"),
    path('recuperar-contraseña/',recContra,name="recuperarContrasena"),
    path('inicio/', inicio,name="inicio"),
    path('perfil/',perfil,name="perfil"),
    path('precioRp/',apirest, name="api"),
    path('ayuda/',paginaAyuda, name="ayuda"),
    path('ayuda2/', ayuda, name="ayuda2"),
    path('ayuda3/',ayuda3,name="ayuda3"),
    path('chat/',chat,name="chat"),
    path('games/',games,name="games"),
    path('lista-seguidores/',listaSeguidores,name="listaSeguidores"),
    path('borrar-usuario/<id>',borrarUsuario,name='borrarUsuario'),
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='core/Registro_usuario/login.html'),name='login'),
    path('api/',include(router.urls)),
]