from database.db import getConnection
from models.UserModel import UserModel
from models.RoleModel import RoleModel


class UserController():

    @classmethod
    def login(cls, credential):
        try:

            connection = getConnection()
            authenticated_user = None

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT id, username, role_id FROM users WHERE email = '{}' AND password = '{}'""".format(credential.email, credential.password,))
                row = cursor.fetchone()

                if row != None:
                    authenticated_user = UserModel(
                        row[0], row[1], '', '',  row[2], '')
                    authenticated_user = authenticated_user.to_JSON()

            connection.close()
            return authenticated_user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_role(self, data):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """ INSERT INTO roles (name,created_at)
                        VALUES (%s,%s)
                        RETURNING id""", (data.name, data.created_at)
                )
                insert_id = cursor.fetchone()[0]
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return {'affected_rows': affected_rows, 'insert_id': insert_id}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_roles(self):
        try:

            connection = getConnection()
            roles = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, name, created_at FROM roles")
                resultset = cursor.fetchall()

                for row in resultset:
                    role = RoleModel(row[0], row[1], row[2])
                    roles.append(role.to_JSON())

            connection.close()
            return roles
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_role_by_id(self, id):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, name, created_at FROM roles WHERE id = %s", (id,))
                row = cursor.fetchone()

                role = None
                if row != None:
                    role = RoleModel(row[0], row[1], row[2])
                    role = role.to_JSON()

            connection.close()
            return role
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_user(self, data):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """ INSERT INTO users (username, email, password,role_id,created_at)
                        VALUES (%s,%s,%s,%s,%s)
                        RETURNING id""", (data.username, data.email, data.password, data.role_id, data.created_at)
                )
                insert_id = cursor.fetchone()[0]
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return {'affected_rows': affected_rows, 'insert_id': insert_id}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_users(self):
        try:

            connection = getConnection()
            users = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, username, email, role_id, created_at FROM users")
                resultset = cursor.fetchall()

                for row in resultset:
                    user = UserModel(row[0], row[1], row[2], '*****',
                                     row[3], row[4])
                    users.append(user.to_JSON())

            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user_by_id(self, id):
        try:
            connection = getConnection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, username, email, role_id, created_at FROM users WHERE id = %s", (id,))
                row = cursor.fetchone()

                user = None
                if row != None:
                    user = UserModel(row[0], row[1], row[2], '*****',
                                     row[3], row[4])
                    user = user.to_JSON()

            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)
