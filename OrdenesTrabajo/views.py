from django.shortcuts import render

# Create your views here.
def ordenes_trabajo(request):
    contexto={

    }
    return render(request,'ordenes_trabajo.html',contexto)