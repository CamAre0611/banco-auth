from flask import request, jsonify
from service.login_service import LoginService

class LoginController:
    def login(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        rol = data.get("rol")  # puede venir o no

        if LoginService().validate_credentials(username, password, rol):
            return jsonify({"success": True, "message": "Login exitoso"})
        else:
            return jsonify({"success": False, "message": "Credenciales inválidas"}), 401
