class CuentaBancaria:

    def __init__(self, p_cuenta,s_pcuenta,s_cuenta,s_scuenta):
        self.primera_cuenta = p_cuenta
        self.saldo_pcuenta = s_pcuenta
        self.segunda_cuenta = s_cuenta
        self.saldo_scuenta = s_scuenta
    
    def transferencia_entre_cuentas(self):
        x = input("Ingrese la cuenta del cual quiere transferir: ")

        if x == self.primera_cuenta:
            while True:
                m = float(input("Ingrese el monto a transferir: "))
                if m <= self.saldo_pcuenta:
                    break
                else:
                    print("el monto es mayor al saldo disponible")
            self.saldo_scuenta += m
            self.saldo_pcuenta -= m
        elif x == self.segunda_cuenta:
            while True:
                m = float(input("Ingrese el monto a transferir: "))
                if m <= self.saldo_scuenta:
                    break
                else:
                    print("el monto es mayor al saldo disponible: ")
            self.saldo_pcuenta += m
            self.saldo_scuenta -= m
        else:
            print("Cuenta no reconocida")

    def mostrar(self):
        print(f"1° cuenta: {self.primera_cuenta} saldo: {self.saldo_pcuenta}")
        print(f"2° cuenta: {self.segunda_cuenta} saldo: {self.saldo_scuenta}")



#MAIN
cuenta = CuentaBancaria("2222",3500, "1111", 4000)
cuenta.mostrar()
print()
cuenta.transferencia_entre_cuentas()
print()
cuenta.mostrar()
                 