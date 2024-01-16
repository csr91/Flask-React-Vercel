from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/rct')
def index():
    return render_template('index.html')

@app.route('/apis')
def hello():
    return jsonify(message="Hell from Flask!")