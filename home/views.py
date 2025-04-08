from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import CreateAuto
from home.models import Auto
def homeView(request):
    # return HttpResponse ('hola')
    return render(request, 'homeView.html')

def create_auto(request):
    if request.method == "POST":
        formulario = CreateAuto(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            auto = Auto(marca=info['marca'], modelo=info['modelo'])
            auto.save()
            return redirect('homeView')
    else:
        formulario = CreateAuto()

    return render(request, 'create_auto.html', {'formulario':formulario})