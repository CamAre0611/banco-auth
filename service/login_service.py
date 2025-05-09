class LoginService:
    def validate_credentials(self, username, password):
        return username == "admin" and password == "1234"
