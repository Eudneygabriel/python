from flask import Flask, render_template, redirect, url_for # type: ignore

app = Flask(__name__)

# Variável global para controlar a visibilidade do menu
show_menu = False
@app.route('/')
def index():       
    # Passa o estado do menu e modais para o template
    return render_template('index.html', show_menu=show_menu)



# Outras páginas do seu site
@app.route('/pagina1')
def pagina1():
    return render_template('Micro services.html')

@app.route('/pagina2')
def pagina2():
    return render_template('API_gateway.html')

@app.route('/pagina3')
def pagina3():
    return render_template('Administração de Redes Locais.html')

@app.route('/pagina4')
def pagina4():
    return render_template('banco de dados.html')

@app.route('/pagina5')
def pagina5():
    return render_template('java.html')

@app.route('/pagina6')
def pagina6():
    return render_template('c++.html')

@app.route('/pagina7')
def pagina7():
    return render_template('processamento computacional.html')

@app.route('/pagina8')
def pagina8():
    return render_template('python.html')

@app.route('/pagina9')
def pagina9():
    return render_template('PGD.html')

@app.route('/pagina10')
def pagina10():
    return render_template('documentaçao.html')

@app.route('/pagina11')
def pagina11():
    return render_template('Organização de um Computador.html')

@app.route('/pagina12')
def pagina12():
    return render_template('Componentes do Computador.html')

@app.route('/pagina13')
def pagina13():
    return render_template('Processador.html')

@app.route('/pagina14')
def pagina14():
    return render_template('Unidade de memória.html')

if __name__ == '__main__':
    app.run(debug=True)
