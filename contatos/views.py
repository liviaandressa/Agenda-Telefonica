from django.shortcuts import render
from .models import Contato

def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        'contatos': contatos
        
    })

def ver_contato(request, contato_id):
    contato = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        'contato': contato
        
    })