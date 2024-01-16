from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apu')
def hello():
    return jsonify(message="Hellooo from Flask!")

@app.route('/apa/hello')
def helloo():
    return jsonify(message="Hellooo from Flask api hello!")