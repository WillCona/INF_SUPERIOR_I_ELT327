    

cadena = ""

n = int(input("ingrese un numero del 1 al 9: "))

for _ in range(1, n+1):
    cadena += str(_)

for i in range(n):
        print(cadena)
        cadena = cadena[1:] + cadena[0]
