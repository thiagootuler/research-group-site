from django.shortcuts import render
from site_app.models import CarregaDados

dados = CarregaDados()


def index(request, conteudo=dados.apresentacao):
    return render(request, 'index.html', {'conteudo': conteudo})


def publicacoes(request, conteudo=dados.publicacoes):
    return render(request, 'publicacoes.html', {'titulo': "Publicações", 'conteudo': conteudo})


def artigo(request, conteudo=dados.artigo):
    return render(request, 'artigo.html', {'conteudo': conteudo})


def membros(request, conteudo=dados.membros):
    return render(request, 'membros.html', {'titulo': "Equipe de pesquisadores", 'conteudo': conteudo})


def contato(request, conteudo=dados.contato):
    return render(request, 'contato.html', {'titulo': "Formas de contato", 'conteudo': conteudo})
