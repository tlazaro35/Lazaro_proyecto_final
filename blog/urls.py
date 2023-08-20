"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app_blog.views import bienvenida , Informacion , Contacto , Ver_mas , Es_un , Certificaciones , Otros
from app_usuarios.views import registro , registrado , lista_usuarios , eliminar_usuario , editar_usuario
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenida),
    path('informacion/', Informacion),
    path('contacto/' , Contacto),
    path('pages/' , Ver_mas),
    path('es_un/' , Es_un),
    path('cert/' , Certificaciones),
    path('otros/' , Otros),
    path('registrado/' , registrado),
    path('lista_usuarios/' , lista_usuarios , name='lista_usuarios'),
    path('eliminar_usuario/<int:usuario_id>/', eliminar_usuario, name='eliminar_usuario'),
    path('editar_usuario/<int:pk>/', editar_usuario, name='editar_usuario'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/' , registro),
]

    
    
