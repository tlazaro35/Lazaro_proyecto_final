from django.shortcuts import render, redirect , get_object_or_404
from .forms import UsuarioFormulario
from .models import Usuario
from django.contrib.auth import login , logout
from django.contrib.auth import views
from django.test import TestCase

def registrado(request) :
    http_response = render(
        request=request,
        template_name='registrado.html',
        context={},
    )
    return http_response


def registro(request):
    if request.method == 'POST':
        form = UsuarioFormulario(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])  
            user.save()
            login(request, user)
            return redirect('/registrado/')
    else:
        form = UsuarioFormulario()
    
    return render(request, 'registro.html', {'formulario': form})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'lista_usuarios.html', context)

def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return redirect('lista_usuarios')

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    
    if request.method == "POST":
        formulario = UsuarioFormulario(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_usuarios')
    else:
        formulario = UsuarioFormulario(instance=usuario)
    
    return render(request, 'editar_usuario.html', {'formulario': formulario})


class usuariotest(TestCase):
    
    def test_crear_usuario(self):
        Usuario = Usuario(Usuario="Juan" , Trabajo = "Administrador")
        Usuario.save()
        
        self.assertEqual(Usuario.objects.count(), 1)
        self.assertEqual(Usuario.Usuario, 'Juan')
        self.assertEqual(Usuario.Trabajo, 'Administrador')
        
        