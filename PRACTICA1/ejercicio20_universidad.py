from ejercicio20_institucion import InstitucionEducativa

class Universidad(InstitucionEducativa):
    def __init__(self, nombre, tipo, nro_profesores, nro_estudiantes, nro_carreras):
        super().__init__(nombre, tipo, nro_profesores, nro_estudiantes)
        self.__nro_carreras = nro_carreras
    
    def get_nro_carreras(self):
        return self.__nro_carreras
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Carreras: {self.__nro_carreras}")
        print("----------------------------")
