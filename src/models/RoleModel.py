class RoleModel():

    def __init__(self, id: 0, name, created_at) -> None:
        self.id = id
        self.name = name
        self.created_at = created_at

    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at
        }
