class PredictModel():

    def __init__(self, id: 0, user_id, genero, propietario_auto, propietario_propiedad, ninos, ingresos_anuales, tipo_ingreso, educacion, estado_civil, tipo_vivienda, fecha_nacimiento, fecha_ingreso_empleo, celular, telefono_casa, telefono_trabajo, email, tipo_ocupacion, miembros_familia, resultado, created_at) -> None:
        self.id = id
        self.user_id = user_id
        self.genero = genero
        self.propietario_auto = propietario_auto
        self.propietario_propiedad = propietario_propiedad
        self.ninos = ninos
        self.ingresos_anuales = ingresos_anuales
        self.tipo_ingreso = tipo_ingreso
        self.educacion = educacion
        self.estado_civil = estado_civil
        self.tipo_vivienda = tipo_vivienda
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso_empleo = fecha_ingreso_empleo
        self.celular = celular
        self.telefono_casa = telefono_casa
        self.telefono_trabajo = telefono_trabajo
        self.email = email
        self.tipo_ocupacion = tipo_ocupacion
        self.miembros_familia = miembros_familia
        self.resultado = resultado
        self.created_at = created_at

    def to_JSON(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'genero': self.genero,
            'propietario_auto': self.propietario_auto,
            'propietario_propiedad': self.propietario_propiedad,
            'ninos': self.ninos,
            'ingresos_anuales': self.ingresos_anuales,
            'tipo_ingreso': self.tipo_ingreso,
            'educacion': self.educacion,
            'estado_civil': self.estado_civil,
            'tipo_vivienda': self.tipo_vivienda,
            'fecha_nacimiento': self.fecha_nacimiento,
            'fecha_ingreso_empleo': self.fecha_ingreso_empleo,
            'celular': self.celular,
            'telefono_casa': self.telefono_casa,
            'telefono_trabajo': self.telefono_trabajo,
            'email': self.email,
            'tipo_ocupacion': self.tipo_ocupacion,
            'miembros_familia': self.miembros_familia,
            'resultado': self.resultado,
            'created_at': self.created_at
        }
