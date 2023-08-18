from datetime import datetime

from django.shortcuts import render
from django.http import  HttpResponse

def bienvenida(request) :
    http_response = render(
        request=request,
        template_name='padre.html',
        context={},
    )
    return http_response

def Informacion(request) :
    http_response = render(
        request=request,
        template_name='informacion.html',
        context={},
    )
    return http_response

def Contacto(request) :
    http_response = render(
        request=request,
        template_name='contacto.html',
        context={},
    )
    return http_response

def Ver_mas(request) :
    http_response = render(
        request=request,
        template_name='pages.html',
        context={},
    )
    return http_response

def Es_un(request) :
    http_response = render(
        request=request,
        template_name='es_un.html',
        context={},
    )
    return http_response

def Certificaciones(request) :
    http_response = render(
        request=request,
        template_name='certificaciones.html',
        context={},
    )
    return http_response

def Otros(request) :
    http_response = render(
        request=request,
        template_name='otros.html',
        context={},
    )
    return http_response


def mi_vista(request):
    archivo = "blog\media\archivo1.pdf" 
    context = {'archivo1': archivo}
    return render(request, 'archivo1.html', context)

def mi_vista(request):
    archivo = "blog\media\archivo2.pdf" 
    context = {'archivo2': archivo}
    return render(request, 'archivo2.html', context)

def mi_vista(request):
    archivo = "blog\media\archivo3.pdf" 
    context = {'archivo3': archivo}
    return render(request, 'archivo3.html', context)

def mi_vista(request):
    archivo = "blog\media\archivo4.pdf" 
    context = {'archivo4': archivo}
    return render(request, 'archivo4.html', context)

def mi_vista(request):
    archivo = "blog\media\archivo5.pdf" 
    context = {'archivo5': archivo}
    return render(request, 'archivo5.html', context)