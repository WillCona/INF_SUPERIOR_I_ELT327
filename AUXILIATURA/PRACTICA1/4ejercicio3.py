class Coche:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._velocidad = 0  # La velocidad inicial es 0

    def acelerar(self):
        self._velocidad += 5

    def frenar(self):
        self._velocidad = max(0, self._velocidad - 5)

    def obtener_velocidad(self):
        return self._velocidad

#MAIN

marca = input("Ingrese marca: ")
modelo = input("Ingrese modelo: ")
mi_coche = Coche(marca, modelo)

mi_coche.acelerar()
mi_coche.frenar()

print("velocidad:", mi_coche.obtener_velocidad())
