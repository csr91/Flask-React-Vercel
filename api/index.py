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
    return jsonify(message="Hello from Flask!")

@app.route('/api/hello')
def hellu():
    return jsonify(message="Hello from Flask from api helllooo!!!")

# Nueva ruta para /otroarchivo
@app.route('/api/otroarchivo')
def otro_archivo():
    return hola_desde_otro_archivo()

def catalogo_cannubis():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "select Idproducto, Idlineadeproducto, Cantidad, Nombre, Shortdesc, vigenciaactivado, diaspublicacion from productos"
    cursor.execute(query)
    catalogo = cursor.fetchall()
    cursor.close()
    conn.close()

    catalogo_json = []
    for producto in catalogo:
        producto_json = {
            'Idproducto': producto[0],
            'Linea': producto[1],
            'Cantidad': producto[2],
            'Nombre': producto[3],
            'Descripcion': producto[4],
            'Vigencia': producto[5],
            'Diaspublicacion': producto[6],
        }
        catalogo_json.append(producto_json)

    # Devolver los productos como respuesta en formato JSON
    return jsonify(catalogo_json)

@app.route('/api/catalogo', methods=['GET'])
def get_catalogo_cannubis():
    return catalogo_cannubis()

db_config = {
    'host': 'bolnbaxunipx24ddxmdb-mysql.services.clever-cloud.com',
    'user': 'u7wbyowvxrhkpjlc',
    'password': 'FrIz7IUBs9YCG9tkD1Up',
    'database': 'bolnbaxunipx24ddxmdb',
    'port': 3306
}