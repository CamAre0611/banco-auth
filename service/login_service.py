class LoginService:
    def validate_credentials(self, username, password):
        try:
            with open("usuarios.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) >= 2:
                        user, pwd = parts[0], parts[1]
                        if user == username and pwd == password:
                            return True
            return False
        except Exception as e:
            print("Error leyendo usuarios.txt:", e)
            return False
