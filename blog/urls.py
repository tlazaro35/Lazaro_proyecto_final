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
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('registro/' , registro),
]

    
    
