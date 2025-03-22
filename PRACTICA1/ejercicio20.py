from ejercicio20_colegio import Colegio
from ejercicio20_instituto import Instituto
from ejercicio20_universidad import Universidad


# Instanciar 3 objetos de cada clase
colegio1 = Colegio("Colegio ABC", "Privado", 30, 500, "Mañana")
colegio2 = Colegio("Colegio XYZ", "Público", 40, 600, "Tarde")
colegio3 = Colegio("Colegio Delta", "Privado", 25, 450, "Nocturno")

instituto1 = Instituto("Instituto Tecno", "Privado", 50, 800, 10)
instituto2 = Instituto("Instituto Pro", "Público", 40, 700, 8)
instituto3 = Instituto("Instituto Sigma", "Privado", 60, 900, 12)

universidad1 = Universidad("Universidad Nacional", "Público", 200, 5000, 30)
universidad2 = Universidad("Universidad Privada", "Privado", 150, 4000, 25)
universidad3 = Universidad("Universidad Estatal", "Público", 180, 4500, 28)

# Mostrar un colegio, un instituto y una universidad
print("=== Información de un Colegio ===")
colegio1.mostrar_info()

print("=== Información de un Instituto ===")
instituto1.mostrar_info()

print("=== Información de una Universidad ===")
universidad1.mostrar_info()
