from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/publicacoes")
def publicacoes():
    return render_template('publicacoes.html')

@app.route("/artigo")
def artigo():
    return render_template('artigo.html')

@app.route("/membros")
def membros():
    return render_template('membros.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')

if __name__ == "__main__":
  app.run(debug=True)
