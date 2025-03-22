# Clase base Cuenta
class Cuenta:
    def __init__(self, saldo=0.0, tasa_anual=0.0):
        self.saldo = saldo
        self.nro_consignaciones = 0
        self.nro_retiros = 0
        self.tasa_anual = tasa_anual
        self.comision_mensual = 0.0

    def consignar(self, monto):
        if monto > 0:
            self.saldo += monto
            self.nro_consignaciones += 1
            print(f"Consignación exitosa. Nuevo saldo: {self.saldo}")
        else:
            print("El monto debe ser mayor a cero.")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            self.nro_retiros += 1
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente o monto inválido.")

    def extracto_mensual(self):
        self.saldo -= self.comision_mensual
        print(f"Extracto mensual aplicado. Saldo final: {self.saldo}")

    def imprimir(self):
        print(f"\nSaldo: {self.saldo}")
        print(f"Número de consignaciones: {self.nro_consignaciones}")
        print(f"Número de retiros: {self.nro_retiros}")
        print(f"Tasa anual: {self.tasa_anual}%")
        print(f"Comisión mensual: {self.comision_mensual}\n")


# Clase hija CuentaAhorros
class CuentaAhorros(Cuenta):
    def __init__(self, saldo=0.0, tasa_anual=0.0, activa=False):
        super().__init__(saldo, tasa_anual)
        self.activa = activa if saldo > 0 else False

    def extracto_mensual(self):
        if self.nro_retiros > 4:  # Se cobra una comisión si hay más de 4 retiros
            self.comision_mensual += 5.0
        super().extracto_mensual()

    def imprimir(self):
        super().imprimir()
        print(f"Cuenta Activa: {'Sí' if self.activa else 'No'}\n")


# Clase hija CuentaCorriente
class CuentaCorriente(Cuenta):
    def __init__(self, saldo=0.0, tasa_anual=0.0, sobregiro=0.0):
        super().__init__(saldo, tasa_anual)
        self.sobregiro = sobregiro

    def retirar(self, monto):
        if monto > self.saldo:
            self.sobregiro += (monto - self.saldo)
            self.saldo = 0
        else:
            super().retirar(monto)

    def extracto_mensual(self):
        if self.sobregiro > 0:
            self.saldo -= self.sobregiro
            self.sobregiro = 0
        super().extracto_mensual()

    def imprimir(self):
        super().imprimir()
        print(f"Saldo de sobregiro: {self.sobregiro}\n")


# Instanciación de objetos
cuenta1 = CuentaAhorros(saldo=500, tasa_anual=3.5, activa=True)
cuenta2 = CuentaCorriente(saldo=1000, tasa_anual=2.5, sobregiro=200)
cuenta3 = CuentaAhorros(saldo=0, tasa_anual=4.0, activa=False)

# Operaciones con las cuentas
cuenta1.consignar(200)
cuenta1.retirar(100)
cuenta1.extracto_mensual()
cuenta1.imprimir()

cuenta2.retirar(1200)
cuenta2.extracto_mensual()
cuenta2.imprimir()

cuenta3.consignar(50)
cuenta3.retirar(20)
cuenta3.extracto_mensual()
cuenta3.imprimir()
