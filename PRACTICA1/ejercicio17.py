class ArticuloCientifico:
    def __init__(self, titulo, autor, palabras_clave, publicacion, anio, resumen):
        self.titulo = titulo
        self.autor = autor
        self.palabras_clave = palabras_clave
        self.publicacion = publicacion
        self.anio = anio
        self.resumen = resumen

    def mostrar_articulo(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Palabras Clave: {self.palabras_clave}")
        print(f"Publicación: {self.publicacion}")
        print(f"Año: {self.anio}")
        print(f"Resumen: {self.resumen}")
        print("-" * 40)


# Lista para almacenar los artículos
articulos = []

# Crear e instanciar N objetos
N = int(input("Ingrese la cantidad de artículos científicos: "))

for i in range(N):
    print(f"\nRegistro del artículo {i+1}:")
    titulo = input("Título: ")
    autor = input("Autor: ")
    palabras_clave = input("Palabras Clave: ")
    publicacion = input("Publicación: ")
    anio = int(input("Año: "))
    resumen = input("Resumen: ")

    articulo = ArticuloCientifico(titulo, autor, palabras_clave, publicacion, anio, resumen)
    articulos.append(articulo)

# Mostrar todos los artículos almacenados
print("\nLista de artículos científicos registrados:\n")
for articulo in articulos:
    articulo.mostrar_articulo()
