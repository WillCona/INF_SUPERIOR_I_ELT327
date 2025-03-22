def ordenar(vector):
    n = len(vector)
    for i in range(n):
        for j in range(0, n - i - 1):
            if vector[j] > vector[j + 1]: 
                vector[j], vector[j + 1] = vector[j + 1], vector[j]
    return vector



vector = list(map(int, input().split()))

vector_ordenado = ordenar(vector)

promedio = (vector_ordenado[1]+vector_ordenado[2]+vector_ordenado[3])//3

print(f"Nota eliminada: {vector_ordenado[0]} Promedio: {promedio}")