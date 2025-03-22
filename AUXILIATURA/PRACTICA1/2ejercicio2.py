

while True:
    n = int(input("Ingrese N del 1 al 9:"))
    if n >=1 and n <= 9:
        break

for i in range(5, 0,-1):
    for j in range(1,i+1):
        print(j, end = "")
    print()
