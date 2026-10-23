from django.shortcuts import render


def inicio(request):
    clientes = [
        {"nombre": "Ana", "plan": "Integral"},
        {"nombre": "Carlos", "plan": "Familiar"},
        {"nombre": "Laura", "plan": "Básico"},
    ]

    contexto = {
        "nombre_empresa": "Mi empresa",
        "clientes": clientes,
    }

    return render(request, "core/inicio.html", contexto)