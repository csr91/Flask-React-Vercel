from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/api')
def hello():
    return jsonify(message="Hell from Flaskkkkk!")

@app.route('/api/hello')
def hellu():
    return jsonify(message="Hello from Flask from api helllooo!!!")