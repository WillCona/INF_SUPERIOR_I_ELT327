class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self, repeticiones = 1):
        print("Guau! " * repeticiones)  

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")

class Pato(Animal):
    def hacer_sonido(self):
        print("Cuac!")

class Vaca(Animal):
    def hacer_sonido(self):
        print("Mu!")

# Ejemplo de uso
perro = Perro()
perro.hacer_sonido()  
perro.hacer_sonido(3)  
print()
gato = Gato()
gato.hacer_sonido()  
print()
pato = Pato()
pato.hacer_sonido()  
print()
vaca = Vaca()
vaca.hacer_sonido() 