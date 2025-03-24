while True:
    char = input("Ingrese un carácter entre 'a' e 'i': ")
    if len(char) == 1 and 'a' <= char <= 'i':
        break
    print("Inválido. Debe ingresar un solo carácter entre 'a' e 'i'.")

max_char = ord(char)  

# Superior
for i in range(ord('a'), max_char + 1):
    espacios = (max_char - i) * 2  
    print(" " * espacios, end="")
    for j in range(ord('a'), i + 1):
        print(chr(j), end=" ")
    for j in range(i - 1, ord('a') - 1, -1):
        print(chr(j), end=" ")
    print()

# Inferior
for i in range(max_char - 1, ord('a') - 1, -1):
    espacios = (max_char - i) * 2  
    print(" " * espacios, end="")
    for j in range(ord('a'), i + 1):
        print(chr(j), end=" ")
    for j in range(i - 1, ord('a') - 1, -1):
        print(chr(j), end=" ")
    print()
    