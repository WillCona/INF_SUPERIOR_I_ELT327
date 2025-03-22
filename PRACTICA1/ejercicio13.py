# Leer el número de pacientes
num_pacientes = int(input("Ingrese el número de pacientes: "))

total_edad = 0
num_ingresados = 0
edad_ingresados = 0
num_operados = 0
edad_operados = 0

# Leer la edad y el índice de cada paciente
for _ in range(num_pacientes):
    edad = int(input("Ingrese la edad del paciente: "))
    indice = float(input("Ingrese el índice del paciente: "))
    
    total_edad += edad
    
    if indice > 0.6:
        num_ingresados += 1
        edad_ingresados += edad
    
    if indice > 0.9:
        num_operados += 1
        edad_operados += edad

# Calcular y mostrar las edades medias
print("Edad media de los pacientes analizados:", total_edad / num_pacientes)
print("Edad media de los ingresados:", (edad_ingresados / num_ingresados) if num_ingresados > 0 else "No existe")
print("Edad media de los operados:", (edad_operados / num_operados) if num_operados > 0 else "No existe")
