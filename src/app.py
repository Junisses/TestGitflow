from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Bienvenido"

@app.route('/hello')
def saludo():
    return "Hola mundo"

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    return f"La suma es: {str(a + b)}"

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a: int, b: int):
    result = float(a * b)
    return f"El resultado de la multiplicación es: {str(result)}"
