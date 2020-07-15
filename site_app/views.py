from django.shortcuts import render
from site_app.models import apresentacao, artigo, membro, contato


def index(request, apresentacao=apresentacao):
    return render(request, 'index.html', {'conteudo': apresentacao})

def publicacoes(request, publicacoes=[artigo] * 3):
    return render(request, 'publicacoes.html', {'titulo': "Publicações", 'conteudo': publicacoes})

def artigo(request, artigo=artigo):
    return render(request, 'artigo.html', {'conteudo': artigo})

def membros(request, membros=[membro for i in range(7)]):
    return render(request, 'membros.html', {'titulo':"Equipe de pesquisadores", 'conteudo': membros})

def contato(request, contato=contato):
    return render(request, 'contato.html', {'titulo': "Formas de contato", 'conteudo': contato})
