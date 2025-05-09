from flask import Flask
from routes import login_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(login_blueprint)

if __name__ == '__main__':
    print("=== RUTAS ACTIVAS ===")
    for rule in app.url_map.iter_rules():
        print(rule)
    app.run(host='0.0.0.0', port=5002)
