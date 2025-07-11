import os
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ CCTV Stream Host is Running"

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('hls', path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # use Railway's assigned port
    app.run(host='0.0.0.0', port=port)
