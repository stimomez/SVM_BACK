
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


class SMV:
    def __init__(self):
        self.df = pd.read_csv("./Credit_card.csv")
        self.preprocesar_datos()
        self.dividir_datos()

    def preprocesar_datos(self):
        # Preprocesamiento de datos
        self.df['propietario_auto'] = (
            self.df['propietario_auto'] == 'Y').astype(int)
        self.df['propietario_propiedad'] = (
            self.df['propietario_propiedad'] == 'Y').astype(int)
        # Eliminación de columnas no deseadas
        self.X = self.df.drop(['Ind_ID', 'genero', 'tipo_ingreso', 'educacion', 'estado_civil',
                               'tipo_vivienda', 'telefono_trabajo', 'telefono', 'email',
                               'tipo_ocupacion', 'respuesta'], axis='columns')
        # Llenar valores nulos con un valor específico, por ejemplo, 0
        self.X = self.X.fillna(0)
        self.y = self.df['respuesta']

    def dividir_datos(self):
        # División de datos en conjuntos de entrenamiento y prueba
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2
        )

    def entrenar_modelo(self, C=10):
        # Entrenamiento del modelo
        self.model = SVC(C=C)
        self.model.fit(self.X_train, self.y_train)

    def obtener_puntuacion(self):
        # Obtener la puntuación del modelo
        return self.model.score(self.X_test, self.y_test)

    def predecir(self, propietario_auto, propietario_propiedad, niños, ingresos_anuales,
                 conteo_cumpleaños, dias_empleado, telefono_movil, miembros_familia):
        # Realizar predicción con el modelo
        result = self.model.predict([[propietario_auto, propietario_propiedad, niños, ingresos_anuales,
                                    conteo_cumpleaños, dias_empleado, telefono_movil, miembros_familia]])

        return result

# df = pd.read_csv("Credit_card.csv")
# df.head(5)

# # df.info()

# # Asignar 1 a 'y' y 0 a 'n'
# df['propietario_auto'] = (df['propietario_auto'] == 'Y').astype(int)
# df['propietario_propiedad'] = (df['propietario_propiedad'] == 'Y').astype(int)
# # Se escoge la última columna como variables de salida
# y = df.respuesta
# X = df.drop(['Ind_ID', 'genero', 'tipo_ingreso', 'educacion', 'estado_civil', 'tipo_vivienda',
#             'telefono_trabajo', 'telefono', 'email', 'tipo_ocupacion', 'respuesta'], axis='columns')
# # Llenar valores nulos con un valor específico, por ejemplo, 0
# X = X.fillna(0)
# # Se separa el dataset en datos de entrenamiento (80%) y prueba (20%)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# len(X_train), len(X_test)

# model = SVC(C=10)

# model.fit(X_train, y_train)

# model.score(X_test, y_test)


# def predict(propietario_auto, propietario_propiedad, niños, ingresos_anuales, conteo_cumpleaños, dias_empleado, telefono_movil, miembros_familia):

#     model.predict([[propietario_auto, propietario_propiedad, niños, ingresos_anuales,
#                   conteo_cumpleaños, dias_empleado, telefono_movil, miembros_familia]])
