#Definir una tupla con 10 edades de personas.

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Definir una lista vacía para almacenar las edades
edades = []

#Solicitar al usuario que ingrese 10 edades
for i in range(10):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    edades.append(edad)

#Convertir la lista de edades en una tupla
edades_tupla = tuple(edades)

#Contar cuántas edades son superiores a 20
personas_mayores_20 = sum(1 for edad in edades_tupla if edad > 20)

#Imprimir el resultado
print(f"\nCantidad de personas con edades superiores a 20: {personas_mayores_20}")
