class Contacto:
    def __init__(self, nombre, apellido, nro_celular, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.nro_celular = nro_celular
        self.correo = correo

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Celular: {self.nro_celular}")
        print(f"Correo: {self.correo}")
        print("-" * 40)


class AgendaTelefonica:
    def __init__(self):
        self.contactos = []  # Lista para almacenar los contactos

    def adicionar_contacto(self, contacto):
        self.contactos.append(contacto)
        print(f"Contacto {contacto.nombre} {contacto.apellido} agregado con éxito.\n")

    def mostrar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.\n")
        else:
            print("\nLista de contactos:")
            for contacto in self.contactos:
                contacto.mostrar_info()

    def buscar_contacto(self, nombre):
        print(f"\nBuscando contacto con nombre: {nombre}...")
        encontrados = [c for c in self.contactos if c.nombre.lower() == nombre.lower()]
        
        if encontrados:
            print("\nContacto(s) encontrado(s):")
            for contacto in encontrados:
                contacto.mostrar_info()
        else:
            print("No se encontró ningún contacto con ese nombre.\n")


# Crear una agenda
agenda = AgendaTelefonica()

# Solicitar la cantidad de contactos a agregar
N = int(input("Ingrese la cantidad de contactos a registrar: "))

# Adicionar contactos a la agenda
for i in range(N):
    print(f"\nRegistro del contacto {i+1}:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    nro_celular = input("Número de celular: ")
    correo = input("Correo: ")

    nuevo_contacto = Contacto(nombre, apellido, nro_celular, correo)
    agenda.adicionar_contacto(nuevo_contacto)

# Mostrar todos los contactos registrados
agenda.mostrar_contactos()
print("-"*30)
# Buscar un contacto por nombre
nombre_buscar = input("\nIngrese el nombre del contacto a buscar: ")
agenda.buscar_contacto(nombre_buscar)
