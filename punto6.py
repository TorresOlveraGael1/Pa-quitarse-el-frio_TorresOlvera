#Escribir un pequeño programa 

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Ingresar el año actual
anio_actual = int(input("Ingresa el año en curso: "))

#Definir una lista para almacenar la información de las personas
personas = []

#Ingresar datos de tres personas
for i in range(3):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    anio_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
    edad = anio_actual - anio_nacimiento
    personas.append((nombre, anio_nacimiento, edad))

#Imprimir el resultado
print("\nAños que cumplirán las personas durante el año en curso:")
for persona in personas:
    nombre, anio_nacimiento, edad = persona
    print(f"{nombre} nació en {anio_nacimiento} y cumplirá {edad} años.")
