class Opercaciones:

    def __init__(self, p_valor, s_valor):
        
        self.primer_valor = p_valor
        self.segundo_valor = s_valor
    
    def potencia(self):

        print(f"podencia es igual a: {self.primer_valor**self.segundo_valor}")
    def raiz_cuadrada(self):

        print(f"raiz del 1er valor es igual a: {self.primer_valor**1/2}")
        print(f"raiz del 2do valor es igual a: {self.segundo_valor**1/2}")
    def  multiplicacion(self):

        print(f"multitiplicación es igual a: {self.primer_valor*self.segundo_valor}")

    def division(self):
        if self.segundo_valor == 0:
            print(f"denominador es 0 division indeterminado")
        else:
            print(f"division es igual a: {self.primer_valor/self.segundo_valor}")


#main
pv = float(input("primer valor: "))
ps = float(input("segundo valor: "))
op1 = Opercaciones(pv, ps)

op1.potencia()
op1.raiz_cuadrada()
op1.multiplicacion()
op1.division()
        


        
