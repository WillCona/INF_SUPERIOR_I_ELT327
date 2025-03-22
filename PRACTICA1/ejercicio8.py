
n = int(input("Ingresar numero:"))
suma = 0
if n > 9:
    while n > 9:
        d = n % 10
        n = n // 10
        suma += d
        if n < 10:
            suma += n
            n = suma
            suma = 0
print(f"la suma es: {n}")


