from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

layout = """
    <h1> Proyecto Web (LP3) || Oyola Carlos </h1>
    <hr/>
    <ul>
        <li>
            <a href= "/inicio">Inicio</a>
        </li>
        <li>
            <a href= "/saludo">Mensaje de Saludo</a>
        </li>
        <li>
            <a href= "/integrantes">Integrantes</a>
        </li>
    </ul>
    <hr/>
"""

def index(request):
    return render(request, 'index.html')

def saludo(request):
    return render(request,'saludo.html')

def integrantes(request):
    return render(request,'integrantes.html')