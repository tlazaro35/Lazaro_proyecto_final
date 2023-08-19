from django.shortcuts import render, redirect , get_object_or_404
from .forms import UsuarioFormulario
from .models import Usuario

def Registrado(request) :
    http_response = render(
        request=request,
        template_name='registrado.html',
        context={},
    )
    return http_response


def registro(request):
    if request.method == "POST":
        formulario = UsuarioFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/registrado/')  
    else:
        formulario = UsuarioFormulario()
    
    return render(request, 'registro.html', {'formulario': formulario})

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