from flask import Blueprint, request, jsonify
import datetime


# Models
from models.UserModel import UserModel


from models.RoleModel import RoleModel
# from src.models import RoleModel


# Security
from utils.Security import Security
# controllers
from controllers.UserController import UserController


main = Blueprint('user_blueprint', __name__)


@main.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    credential = UserModel('', '', email,
                           password, '', '')

    authenticated_user = UserController.login(credential)

    if (authenticated_user != None):
        encoded_token = Security.generate_token(authenticated_user)
        role = UserController.get_role_by_id(
            int(authenticated_user['role_id']))

        return jsonify({'success': True, 'role': role,  'token': encoded_token}), 200
    else:
        response = jsonify({'message': 'credential invalid'})
        return response, 401


@main.route('/role', methods=['POST'])
def create_role():
    try:
        name = request.json['name']
        # Obtener la fecha y hora actual
        created_at = datetime.datetime.now()

        new_role = RoleModel('', name, created_at)

        res = UserController.create_role(new_role)

        if res['affected_rows'] == 1:
            new_role = RoleModel(res['insert_id'], name, created_at)
            return jsonify(new_role.to_JSON())
        else:
            return jsonify({'message': 'Error on insert'}), 500

    except Exception as ex:
        # error servidor
        return jsonify({'message': str(ex)}), 500


@main.route('/role', methods=['GET'])
def get_Roles():
    try:
        roles = UserController.get_roles()
        return jsonify(roles)
    except Exception as ex:
        # error servidor
        return jsonify({'message': str(ex)}), 500


@main.route('/role/<id>', methods=['GET'])
def get_role_by_id(id):
    try:
        role = UserController.get_role_by_id(id)

        if role != None:
            return jsonify(role)
        else:
            return jsonify({}), 404
    except Exception as ex:
        # error servidor
        return jsonify({'message': str(ex)}), 500


@main.route('/', methods=['POST'])
def create_user():

    has_access = Security.verify_token(request.headers)
    if has_access:
        role = UserController.get_role_by_id(has_access['role_id'])
        if role['name'].lower() == 'admin':
            try:
                username = request.json['username']
                email = request.json['email']
                password = request.json['password']
                role_id = request.json['role_id']
                # Obtener la fecha y hora actual
                created_at = datetime.datetime.now()

                new_user = UserModel('', username, email,
                                     password, role_id, created_at)

                res = UserController.create_user(new_user)

                if res['affected_rows'] == 1:
                    new_user = UserModel(res['insert_id'], username, email,
                                         '*******', role_id, created_at)
                    return jsonify(new_user.to_JSON())
                else:
                    return jsonify({'message': 'Error on insert'}), 500

            except Exception as ex:
                # error servidor
                return jsonify({'message': str(ex)}), 500
        else:
            response = jsonify({'message': 'unauthorized'})
            return response, 401
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401


@main.route('/', methods=['GET'])
def get_users():

    has_access = Security.verify_token(request.headers)

    if has_access:

        role = UserController.get_role_by_id(has_access['role_id'])
        if role['name'].lower() == 'admin':
            try:
                users = UserController.get_users()
                return jsonify(users)

            except Exception as ex:
                # error servidor
                return jsonify({'message': str(ex)}), 500
        else:
            response = jsonify({'message': 'unauthorized'})
            return response, 401
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401


@main.route('/<id>', methods=['GET'])
def get_user_by_id(id):
    try:
        role = UserController.get_user_by_id(id)

        if role != None:
            return jsonify(role)
        else:
            return jsonify({}), 404
    except Exception as ex:
        # error servidor
        return jsonify({'message': str(ex)}), 500
