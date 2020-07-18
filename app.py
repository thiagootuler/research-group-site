from flask import Flask, render_template, url_for
from models import CarregaDados
from datetime import datetime

dados = CarregaDados()

app = Flask(__name__)

@app.context_processor
def inject_variables(contato=dados.contato):
    return dict(
        header_title="<strong>NOME</strong> Research Group",
        footer_contact=contato,
        now=datetime.utcnow()
    )

@app.route("/")
def index(apresentacao=dados.apresentacao):
    return render_template('index.html', conteudo=apresentacao)

@app.route("/publicacoes")
def publicacoes(publicacoes=dados.publicacoes):
    return render_template('publicacoes.html', titulo="Publicações", conteudo=publicacoes)

@app.route("/artigo")
def artigo(artigo=dados.artigo):
    return render_template('artigo.html', conteudo=artigo)

@app.route("/membros")
def membros(membros=dados.membros):
    return render_template('membros.html', titulo="Equipe de pesquisadores", conteudo=membros)

@app.route("/contato")
def contato(contato=dados.contato):
    return render_template('contato.html', titulo="Formas de contato", conteudo=contato)

if __name__ == "__main__":
    app.run(debug=True)
