from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ CCTV Stream Host is Running"

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('hls', path)
