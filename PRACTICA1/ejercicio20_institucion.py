class InstitucionEducativa:
    def __init__(self, nombre, tipo, nro_profesores, nro_estudiantes):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__nro_profesores = nro_profesores
        self.__nro_estudiantes = nro_estudiantes
    
    def get_nombre(self):
        return self.__nombre
    
    def get_tipo(self):
        return self.__tipo
    
    def get_nro_profesores(self):
        return self.__nro_profesores
    
    def get_nro_estudiantes(self):
        return self.__nro_estudiantes
    
    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Tipo: {self.__tipo}")
        print(f"Número de Profesores: {self.__nro_profesores}")
        print(f"Número de Estudiantes: {self.__nro_estudiantes}")
