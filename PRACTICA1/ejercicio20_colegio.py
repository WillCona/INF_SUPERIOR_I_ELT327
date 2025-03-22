from ejercicio20_institucion import InstitucionEducativa

class Colegio(InstitucionEducativa):
    def __init__(self, nombre, tipo, nro_profesores, nro_estudiantes, turno):
        super().__init__(nombre, tipo, nro_profesores, nro_estudiantes)
        self.__turno = turno
    
    def get_turno(self):
        return self.__turno
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Turno: {self.__turno}")
        print("----------------------------")
