from flask import jsonify
from service.login_service import LoginService

class LoginController:
    def login(self, username, password):
        if LoginService().validate_credentials(username, password):
            return jsonify({"success": True, "message": "Login exitoso"})
        else:
            return jsonify({"success": False, "message": "Credenciales inválidas"}), 401
