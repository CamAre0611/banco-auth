from flask import request, jsonify
from service.login_service import LoginService

class LoginController:
    def login(self):
        try:
            data = request.get_json()
            username = data.get("username")
            password = data.get("password")
            rol = data.get("rol")  # puede ser None

            if not username or not password:
                return jsonify({"success": False, "message": "Faltan datos"}), 400

            if LoginService().validate_credentials(username, password, rol):
                return jsonify({"success": True, "message": "Login exitoso"})
            else:
                return jsonify({"success": False, "message": "Credenciales inválidas"}), 401
        except Exception as e:
            return jsonify({"success": False, "message": f"Error interno: {str(e)}"}), 500
