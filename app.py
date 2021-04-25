import os

from flask import Flask, render_template, redirect, url_for, flash, request, send_from_directory
from models import CarregaDados, Artigo, Membro
from datetime import datetime
from werkzeug.utils import secure_filename
from utils import ImageEditor

UPLOAD_FOLDER = '/home/thiago/Projetos/gagen/site/uploads'
ALLOWED_EXTENSIONS = {'png'}

dados = CarregaDados()

app = Flask(__name__)
app.config['UPLOAD_FOLDER_PHOTOS'] = UPLOAD_FOLDER + '/membro'

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

@app.route("/publicacoes/artigo")
def artigo(artigo=dados.artigo):
    return render_template('artigo.html', conteudo=artigo)

@app.route("/membros")
def membros(membros=dados.membros):
    return render_template('membros.html', titulo="Equipe de pesquisadores", conteudo=membros)

@app.route("/contato")
def contato(contato=dados.contato):
    return render_template('contato.html', titulo="Formas de contato", conteudo=contato)

@app.route("/publicacoes/artigo/cadastrar")
def artigo_cadastrar():
    return render_template('artigo-cadastrar.html', titulo="Cadastrar artigo")

@app.route("/cadastrar/artigo", methods=['POST',])
def cadastro_artigo():
    artigo=Artigo(
        titulo=request.form['titulo'],
        autores=request.form['autores'].split(","),
        capa="",
        miniatura="",
        resumo=request.form['resumo'],
        citacoes={},
        qualis=request.form['qualis'],
        doi=request.form['doi']
    )
    return render_template('artigo.html', conteudo=artigo)

@app.route("/membros/cadastrar")
def membro_cadastrar():
    return render_template('membro-cadastrar.html', titulo="Cadastrar membro")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/membro/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER_PHOTOS'],
                               filename)

@app.route("/cadastrar/membro", methods=['POST',])
def cadastro_membro():
    nome = request.form['nome']
    foto = url_for('static', filename='images/perfil.png')
    lattes = request.form['lattes']
    nivel = request.form['nivel']
    resumo = request.form['resumo']
    if 'foto' in request.files:
        file = request.files['foto']
        if file.filename != '':
            filename = '_'.join(nome.lower().split(' ')) + os.path.splitext(secure_filename(file.filename))[1]
            path = os.path.join(app.config['UPLOAD_FOLDER_PHOTOS'], filename)
            file.save(path)
            editor = ImageEditor(250, 250, path, path)
            editor.crop()
            editor.resize()
            editor.save()
            foto = url_for('uploaded_file', filename=filename)
            print('{}\n{}'.format(filename,path))
    if not lattes:
        lattes = "http://lattes.cnpq.br/"
    dados.membros.append(Membro(nome, foto, lattes, nivel, resumo))
    # flash("Perfil do membro cadastrado com sucesso.")
    return redirect(url_for('membros'))

if __name__ == "__main__":
    app.run(debug=True)
