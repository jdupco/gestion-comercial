from django.http import HttpResponse


def inicio(request):
    return HttpResponse(
        "Bienvenido al sistema de gestión comercial"
    )