from flask import Flask, render_template, request, jsonify
import json

# Create Flask App
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add-todo', methods=['POST'])
def addTodo():
    data = json.loads(request.data) #Load JSON data from request
    return jsonify(data)