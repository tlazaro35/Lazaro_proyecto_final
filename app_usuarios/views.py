from django.shortcuts import render, redirect
from .forms import UsuarioFormulario

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
