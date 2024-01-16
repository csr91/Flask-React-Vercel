from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def hello():
    return jsonify(message="Hellooo from Flask!")

@app.route('/api/hello')
def hello1():
    return jsonify(message="Hellooo from Flask api hello!")