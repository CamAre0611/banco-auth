from flask import Blueprint
from controller.login_controller import LoginController

login_routes = Blueprint('login_routes', __name__)

login_controller = LoginController()
login_routes.route('/login', methods=['POST'])(login_controller.login)
