#Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Solicitar al usuario que ingrese una lista de nombres
nombres_input = input("Ingresa una lista de nombres separados por coma: ")

#Convertir el string ingresado en una lista de nombres
nombres = [nombre.strip() for nombre in nombres_input.split(',')]

#Solicitar al usuario que ingrese la letra con la que deben comenzar los nombres
letra_buscar = input("Ingresa la letra con la que deben comenzar los nombres: ").lower()

#Contar cuántos nombres comienzan con la letra especificada
cantidad_nombres = sum(1 for nombre in nombres if nombre.lower().startswith(letra_buscar))

#Imprimir el resultado
print(f"\nCantidad de nombres que comienzan con la letra '{letra_buscar.upper()}': {cantidad_nombres}")