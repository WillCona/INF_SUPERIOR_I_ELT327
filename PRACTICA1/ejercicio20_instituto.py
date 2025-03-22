from ejercicio20_institucion import InstitucionEducativa

class Instituto(InstitucionEducativa):
    def __init__(self, nombre, tipo, nro_profesores, nro_estudiantes, nro_especialidades):
        super().__init__(nombre, tipo, nro_profesores, nro_estudiantes)
        self.__nro_especialidades = nro_especialidades
    
    def get_nro_especialidades(self):
        return self.__nro_especialidades
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Especialidades: {self.__nro_especialidades}")
        print("----------------------------")
