from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def inicio(request):
    estudiantes = [ 'Isabella Caballero',
                    'Alejandro Hermitaño',
                    'Joan Palomino',
                    'Pierre Bernaola'
                   ]
    return render(request, 'inicio.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto web con Django (Desde el View)',
        'estudiantes': estudiantes
    })

def saludo(request):
    return render(request, 'saludo.html', {
        'titulo':'Saludo',
        'autor_saludo':'Chavez Tapia, Jhon'
    })

def rango(request):
    a=10
    b=20
    rango_numeros = range(a,b+1)
    return render(request, 'rango.html', {
        'titulo':'Rango',
        'a':a,
        'b':b,
        'rango_numeros':rango_numeros
    })

def rango2(request):
    return render(request, 'rango2.html')