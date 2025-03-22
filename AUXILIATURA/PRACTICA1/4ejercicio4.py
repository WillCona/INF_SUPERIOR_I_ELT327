class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self._titular = titular
        self._saldo = saldo_inicial
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito realizado. Nuevo saldo: {self._saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f"Retiro realizado. Nuevo saldo: {self._saldo}")
        else:
            print("Saldo insuficiente o cantidad no válida.")
    
    def obtener_saldo(self):
        return self._saldo

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, tasa_interes):
        super().__init__(titular, saldo_inicial)  
        self._tasa_interes = tasa_interes  

    def aplicar_interes(self):
        interes = self._saldo * self._tasa_interes / 100
        self._saldo += interes
        print(f"Interés aplicado. Nuevo saldo: {self._saldo}")

# MAIN
titular = input("ingresar titular: ")
inicial = int(input("ingresar saldo inicial: "))
interes = int(input("interes: "))
mi_cuenta = CuentaAhorro(titular, inicial, interes)
print(f"Saldo es: {mi_cuenta.obtener_saldo()}") 
print()
mi_cuenta.depositar(int(input("ingrese monto a depositar: ")))  
mi_cuenta.retirar(int(input("ingrese monto a retirar: "))) 
print()
print("aplicando interes")
mi_cuenta.aplicar_interes() 
print(f"Saldo es: {mi_cuenta.obtener_saldo()}") 
