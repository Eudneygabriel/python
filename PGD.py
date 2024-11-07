# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/pagina9')
def pagina9():
    return render_template('PGD.html')

@app.route('/imagem-grande/<nome_imagem>')
def imagem_grande(nome_imagem):
    # Renderiza uma página que mostra a imagem em tamanho grande
    return render_template('imagem_grande.html', nome_imagem=nome_imagem)


if __name__ == '__main__':
    app.run(debug=True)