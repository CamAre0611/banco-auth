class LoginService:
    def validate_credentials(self, username, password, rol):
        try:
            with open("database/usuarios.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) >= 3:
                        user, pwd, user_rol = parts[0], parts[1], parts[2]
                        print(f"Comparando: input({username}, {password}, {rol}) vs archivo({user}, {pwd}, {user_rol})")
                        if user == username and pwd == password and rol == user_rol:
                            return True
            return False
        except Exception as e:
            print("Error leyendo usuarios.txt:", e)
            return False
