from flask import Flask, render_template

app = Flask(__name__)

artigo = {
    'titulo': "Titulo do artigo",
    'autores': ["Nome do Autor 1", "Nome do Autor 2"],
    'capa': "http://placehold.it/400x200?text=Graphical+Abstract",
    'miniatura': "http://placehold.it/85",
    'resumo': "Atque unde sint velit, omnis iusto sequi. Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis, ratione fuga. Corporis, provident, cum eligendi atque aliquam non saepe laudantium odit soluta nostrum labore, voluptas fuga sit laboriosam veniam eos? Lorem ipsum dolor sit, amet consectetur adipisicing elit. Labore beatae, ut dolorum ipsum consequatur eveniet accusantium, in repellendus repudiandae assumenda animi voluptas quibusdam cumque ad architecto. Fugiat laboriosam eos quas!",
    'citacoes': {
        'BibTeX': '@ARTICLE{nome, AUTHOR = {Nome do Autor},TITLE = {Titulo do artigo},PUBLISHER = {Revista},YEAR = {2020} }',
        'EndNote': '_'
    },
    'classificacao': 0.0,
    'doi': "http://dx.doi.org/..."
}

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/publicacoes")
def publicacoes(artigo=artigo):
    publicacoes = [artigo] * 3
    return render_template('publicacoes.html', titulo="Publicações", conteudo=publicacoes)

@app.route("/artigo")
def artigo(artigo=artigo):
    return render_template('artigo.html', conteudo=artigo)

@app.route("/membros")
def membros():
    return render_template('membros.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')

if __name__ == "__main__":
    app.run(debug=True)
