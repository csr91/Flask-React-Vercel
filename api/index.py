# main.py
import mysql.connector
from flask import Flask, jsonify, render_template
from otroarchivo import hola_desde_otro_archivo  # Importa la función desde el otro archivo

app = Flask(__name__)

@app.route('/rct')
def index():
    return render_template('index.html')

@app.route('/api')
def hello():
    return jsonify(message="Hell from Flask!")

@app.route('/api/hello')
def hellu():
    return jsonify(message="Hell from Flask from api helllooo!!!")

# Nueva ruta para /otroarchivo
@app.route('/api/otroarchivo')
def otro_archivo():
    return hola_desde_otro_archivo()

if __name__ == '__main__':
    app.run(debug=True)