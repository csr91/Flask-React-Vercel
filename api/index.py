from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/rct')
def index():
    return render_template('index.html')

@app.route('/api')
def hello():
    return jsonify(message="Hell from Flask!")

@app.route('/api/hello')
def hellu():
    return jsonify(message="Hello from Flask from api helllooo!!!")