from django.shortcuts import render

# Create your views here.
def vista_catalogo_repuestos(request):
    return render(request, 'catalogo_repuestos/lista_repuestos.html')


