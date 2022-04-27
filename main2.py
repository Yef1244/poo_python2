from clases.Escuderia import Escuderia

print("")
print("Digite 1 para ingresar una nueva escuderia")
print("Digite 2 para comprobar cual es la escuderia más cara")
print("Digite 3 para comprobar cuantas escuderias tienen motor Mercedes, cuantas Ferrari y cuantas Renault")
print("")

opcion = 1
escuderias = []
costos = []

while(opcion != 0):
    opcion = int(input("Ingrese una opcion: "))
    if(opcion == 1):
        escuderia = Escuderia()
        escuderia.nombre = input("Ingrese el nombre de la escuderia: ")
        escuderia.motor = input("Ingrese el motor (mercedes/ferrari/renault/honda): ")
        escuderia.piloto = input("Ingrese el nombre del piloto: ")
        escuderia.costoAnual = int(input("Ingrese el costo anual: "))
        escuderias.append(escuderia)
        costos.append(escuderia.costoAnual)
    elif(opcion == 2):
        costoMayorIter = iter(costos)
        costoMayor = max(costoMayorIter)
        print(f"La escudería más cara es de {costoMayor}$")
    elif(opcion == 3):
        print("test")
else:
    print("Se cerró el menú")