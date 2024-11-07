from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Variável global para controlar a visibilidade do menu
show_menu = False

@app.route('/')
def index():
    # Passa o estado do menu para o template
    return render_template('index.html', show_menu=show_menu)

@app.route('/toggle-menu')
def toggle_menu():
    global show_menu
    # Alterna o estado do menu
    show_menu = not show_menu
    return redirect(url_for('index'))  # Redireciona de volta para a página principal

# Página 1
@app.route('/pagina1')
def pagina1():
    return render_template('Micro services.html')

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

# Página 9
@app.route('/pagina9')
def pagina9():
    return render_template('PGD.html')

# Página 10
@app.route('/pagina10')
def pagina10():
    return render_template('Documentaçao.html')

# Página 11
@app.route('/pagina11')
def pagina11():
    return render_template('Organização de um Computador.html')

# Página 12
@app.route('/pagina12')
def pagina12():
    return render_template('Componentes do Computador.html')

# Página 13
@app.route('/pagina13')
def pagina13():
    return render_template('Processador.html')

# Página 14
@app.route('/pagina14')
def pagina14():
    return render_template('Unidade de memória.html')

if __name__ == '__main__':
    app.run(debug=True)
