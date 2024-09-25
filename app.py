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

if __name__ == '__main__':
    app.run(debug=True)
