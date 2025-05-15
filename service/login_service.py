class LoginService:
    def validate_credentials(self, username, password, rol=None):
        try:
            with open('usuarios.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        user, passw, stored_rol = parts
                        if user == username and passw == password:
                            if rol is None or rol == stored_rol:
                                return True
            return False
        except Exception as e:
            print(f"Error leyendo usuarios.txt: {e}")
            return False
