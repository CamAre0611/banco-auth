# routes.py
from flask import Blueprint, request, jsonify
from controller.login_controller import LoginController

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    return LoginController().login(username, password)
