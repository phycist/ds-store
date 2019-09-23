#############biblioteca##########################
from django.shortcuts import render

#################################################
# criar as paginas aqui
#home
def home(request):
    return render(request, 'loja/home.html')

#sobre
def sobre(request):
    return render(request, 'loja/sobre.html')

#masculino
def masculino(request):
    return render(request, 'loja/produtos/masculino.html')


# feminino 
def feminino(request):
    return render(request, 'loja/produtos/feminino.html')
