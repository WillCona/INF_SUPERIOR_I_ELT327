

cad = input("Ingrese cadena: ")
dic = {} 

for i in range(len(cad)):
    if cad[i] in dic:
        dic[cad[i]] = dic[cad[i]] + 1
    else:
        dic[cad[i]] = 1


for i in dic.items():
    print(f"{i[0]}: {i[1]}")