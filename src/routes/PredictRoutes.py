from flask import Blueprint, request, jsonify
import datetime


# Models
from models.UserModel import UserModel

from models.PredictModel import PredictModel
# from src.models import RoleModel


# Security
from utils.Security import Security
# controllers
from controllers.PredictController import PredictController
from controllers.UserController import UserController


main = Blueprint('predict_blueprint', __name__)


@main.route('/svm', methods=['POST'])
def create_predict():
    has_access = Security.verify_token(request.headers)
    if has_access:

        role = UserController.get_role_by_id(has_access['role_id'])
        if role['name'].lower() == 'comun':
            try:
                genero = request.json['genero']
                propietario_auto = request.json['propietario_auto']
                propietario_propiedad = request.json['propietario_propiedad']
                ninos = request.json['ninos']
                ingresos_anuales = request.json['ingresos_anuales']
                tipo_ingreso = request.json['tipo_ingreso']
                educacion = request.json['educacion']
                estado_civil = request.json['estado_civil']
                tipo_vivienda = request.json['tipo_vivienda']
                fecha_nacimiento = request.json['fecha_nacimiento']
                fecha_ingreso_empleo = request.json['fecha_ingreso_empleo']
                celular = request.json['celular']
                telefono_casa = request.json['telefono_casa']
                telefono_trabajo = request.json['telefono_trabajo']
                email = request.json['email']
                tipo_ocupacion = request.json['tipo_ocupacion']
                miembros_familia = request.json['miembros_familia']
                created_at = datetime.datetime.now()

                data = PredictModel('', has_access['id'], genero, propietario_auto, propietario_propiedad,
                                    ninos, ingresos_anuales, tipo_ingreso, educacion, estado_civil, tipo_vivienda, fecha_nacimiento, fecha_ingreso_empleo, celular, telefono_casa, telefono_trabajo, email, tipo_ocupacion, miembros_familia, "", created_at)

                res = PredictController.predict_svm(data)

                if res['affected_rows'] == 1:

                    new_predict = PredictModel(res['insert_id'], has_access['id'], genero, propietario_auto, propietario_propiedad,
                                               ninos, ingresos_anuales, tipo_ingreso, educacion, estado_civil, tipo_vivienda, fecha_nacimiento, fecha_ingreso_empleo, celular, telefono_casa, telefono_trabajo,  email, tipo_ocupacion, miembros_familia, res['result'], created_at)

                    return jsonify(new_predict.to_JSON())
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


@main.route('/result-svm', methods=['GET'])
def get_Predict_SVM():
    has_access = Security.verify_token(request.headers)
    if has_access:
        role = UserController.get_role_by_id(has_access['role_id'])
        if role['name'].lower() == 'admin':
            try:
                predictions = PredictController.get_predicts()
                url_result_svm = 'https://firebasestorage.googleapis.com/v0/b/inteligencia-artificial-33d03.appspot.com/o/maquinas_soporte_vectorial.html?alt=media&token=e92dac46-142c-4478-9f47-55b58877f7e1'
                return jsonify({'url_result_svm': url_result_svm, 'predictions': predictions})
            except Exception as ex:
                # error servidor
                return jsonify({'message': str(ex)}), 500
        else:
            response = jsonify({'message': 'unauthorized'})
            return response, 401
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401


@main.route('/', methods=['POST'])
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
