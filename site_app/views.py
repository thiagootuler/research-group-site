from django.shortcuts import render

def index(request):
  return render(request, 'index.html')

def publicacoes(request):
  return render(request, 'publicacoes.html')

def artigo(request):
    return render(request, 'artigo.html')

def membros(request):
  return render(request, 'membros.html')

def contato(request):
  return render(request, 'contato.html')