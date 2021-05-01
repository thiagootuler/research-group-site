from django.shortcuts import render
from site_app.models import Apresentacao, Artigo, Membro, Contato


def index(request):
    texto = Apresentacao.objects.last()
    return render(request, 'index.html', {'conteudo': texto})


def publicacoes(request):
    publicacoes = Artigo.objects.all()
    return render(request, 'publicacoes.html', {'titulo': "Publicações", 'conteudo': publicacoes})


def artigo(request, pk):
    artigo = Artigo.objects.get(pk=pk)
    return render(request, 'artigo.html', {'conteudo': artigo})


def membros(request):
    membros = Membro.objects.all()
    return render(request, 'membros.html', {'titulo': "Equipe de pesquisadores", 'conteudo': membros})


def contato(request):
    contato = Contato.objects.all().first()
    return render(request, 'contato.html', {'titulo': "Formas de contato", 'conteudo': contato})
