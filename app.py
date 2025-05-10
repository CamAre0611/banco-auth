import os
from flask import Flask
from routes import login_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(login_blueprint)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Usa el puerto que Render le asigne
    app.run(host='0.0.0.0', port=port)
