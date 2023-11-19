class UserModel():

    def __init__(self, id, username, email, password, role_id, created_at) -> None:
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.role_id = role_id
        self.created_at = created_at

    def to_JSON(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'role_id': self.role_id,
            'created_at': self.created_at
        }
