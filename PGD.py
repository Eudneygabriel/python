# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/pagina9')
def pagina9():
    return render_template('PGD.html')


if __name__ == '__main__':
    app.run(debug=True)