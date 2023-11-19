from database.db import getConnection
from models.PredictModel import PredictModel
from utils.Maquinas_Soporte_Vectorial import SMV
from datetime import datetime


class PredictController():

    @classmethod
    def predict_svm(cls, data):

        smv = SMV()
        smv.entrenar_modelo()

        mobile = 0

        if data.celular != "":
            mobile = 1

        predict_result = smv.predecir(
            data.propietario_auto, data. propietario_propiedad, data.ninos, data.ingresos_anuales, cls.calcular_dias(data.fecha_nacimiento), cls.calcular_dias(data.fecha_ingreso_empleo), mobile, data.miembros_familia)
        result = False
        if predict_result[0] != 0:
            result = True
        try:
            connection = getConnection()
            with connection.cursor() as cursor:
                cursor.execute(
                    """ INSERT INTO predictions (user_id, genero, propietario_auto, propietario_propiedad, ninos, ingresos_anuales, tipo_ingreso, educacion, estado_civil, tipo_vivienda, fecha_nacimiento, fecha_ingreso_empleo, telefono_trabajo, telefono_casa, email, tipo_ocupacion,  miembros_familia, resultado, celular, created_at)
                        VALUES (%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        RETURNING id""", (data.user_id, data.genero, data.propietario_auto, data.propietario_propiedad, data.ninos, data.ingresos_anuales, data.tipo_ingreso, data.educacion, data.estado_civil, data.tipo_vivienda, data.fecha_nacimiento, data.fecha_ingreso_empleo, data.telefono_trabajo, data.telefono_casa, data.email, data.tipo_ocupacion, data.miembros_familia, result, data.celular, data.created_at)
                )
                insert_id = cursor.fetchone()[0]
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return {'affected_rows': affected_rows, 'insert_id': insert_id, 'result': result}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_predicts(self):
        try:

            connection = getConnection()
            predictions = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *  FROM predictions")
                resultset = cursor.fetchall()

                for row in resultset:
                    predictions = PredictModel(row[0], row[1], row[2], row[3],
                                               row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20])
                    predictions.append(predictions.to_JSON())
            print(resultset)
            connection.close()
            return predictions
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def calcular_dias(self, fecha_inicial):
        # Convertir la fecha de nacimiento a un objeto datetime
        fecha_nac = datetime.strptime(fecha_inicial, "%Y-%m-%d")

        # Obtener la fecha actual
        fecha_actual = datetime.now()

        # Calcular la diferencia entre las fechas
        diferencia = fecha_actual - fecha_nac

        # Extraer el número de días de la diferencia
        dias_transcurridos = -diferencia.days

        return dias_transcurridos
