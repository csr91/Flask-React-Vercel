# otroarchivo.py

from flask import jsonify

def hola_desde_otro_archivo():
    return jsonify(message="Hell desde otro archivo!")
