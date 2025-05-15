from controller.login_controller import LoginController
from flask import Blueprint

login_blueprint = Blueprint('login', __name__)

login_controller = LoginController()

@login_blueprint.route("/login", methods=["POST"])
def login():
    return login_controller.login()
