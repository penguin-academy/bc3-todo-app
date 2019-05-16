from flask import Flask, render_template, request, jsonify
import json

# Create Flask App
app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"