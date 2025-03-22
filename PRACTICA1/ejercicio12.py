
n = int(input("Ingrese N: "))

for i in range(n):
    for j in range(n):
        if j == i:
            print("-", end= " ")
        elif i > j:
            print("*", end = " ")
        else:
            print("+", end = " ")
    print()