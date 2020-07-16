from flask import Flask, render_template, url_for
from models import apresentacao, artigo, membro, contato

app = Flask(__name__)

@app.route("/")
def index(apresentacao=apresentacao):
    return render_template('index.html', conteudo=apresentacao)

@app.route("/publicacoes")
def publicacoes(publicacoes=[artigo]*2):
    return render_template('publicacoes.html', titulo="Publicações", conteudo=publicacoes)

@app.route("/artigo")
def artigo(artigo=artigo):
    return render_template('artigo.html', conteudo=artigo)

@app.route("/membros")
def membros(membros=[membro for i in range(7)]):
    return render_template('membros.html', titulo="Equipe de pesquisadores", conteudo=membros)

@app.route("/contato")
def contato(contato=contato):
    return render_template('contato.html', titulo="Formas de contato", conteudo=contato)

if __name__ == "__main__":
    app.run(debug=True)
