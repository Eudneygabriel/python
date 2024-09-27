from flask import Flask, render_template

app = Flask(__name__)

# Página principal com dois botões
@app.route('/')
def index():
    return render_template('index.html')

# Página 1
@app.route('/pagina1')
def pagina1():
    return render_template('Microservices.html')

# Página 2
@app.route('/pagina2')
def pagina2():
    return render_template('API_gateway.html')

# Página 3
@app.route('/pagina3')
def pagina3():
    return render_template('Administração de Redes Locais.html')

# Página 4
@app.route('/pagina4')
def pagina4():
    return render_template('banco de dados.html')

# Página 5
@app.route('/pagina5')
def pagina5():
    return render_template('java.html')

# Página 6
@app.route('/pagina6')
def pagina6():
    return render_template('c++.html')

# Página 7
@app.route('/pagina7')
def pagina7():
    return render_template('processamento computacional.html')

# Página 8
@app.route('/pagina8')
def pagina8():
    return render_template('python.html')

if __name__ == '__main__':
    app.run(debug=True)
