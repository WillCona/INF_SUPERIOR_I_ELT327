

n = int(input("ingresa n: "))

for i in range(n):
    for j in range(n):
        
        if (i+j) == (n-1):
            print("1",end = " ")
        elif (i == 1 and j == 0) or (i == (n-2) and j == (n-1)):
             print("0",end = " ") 
        elif (i+j) == (n-1):
            print("1", end = " ")
        elif i == 0:
            print("0",end = " ")
        elif n-1 == i:
             print("0",end = " ")
        else:
            print(" ", end = " ")

    print()