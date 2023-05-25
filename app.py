from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/g2callback', methods=['POST'])

def foo():

    data = request.json

    print(data)

    return jsonify(data)
