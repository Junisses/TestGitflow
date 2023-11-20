from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "HOLA!"

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    return f"La suma es: {str(a + b)}"
