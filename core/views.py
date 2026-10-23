from django.shortcuts import render

from .models import Cliente


def inicio(request):
    clientes = Cliente.objects.all().order_by("nombre")

    contexto = {
        "nombre_empresa": "Mi empresa",
        "clientes": clientes,
    }

    return render(request, "core/inicio.html", contexto)
