#Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.Un año bisiesto es divisible por 4, pero no por 100

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Definir la función es_bisiesto
def es_bisiesto(año):
    #Un año es bisiesto si es divisible por 4, pero no por 100, o si es divisible por 400
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

#Solicitar al usuario que ingrese un año
año_usuario = int(input("Ingresa un año para saber si es bisiesto: "))

#Llamar a la función y mostrar el resultado
if es_bisiesto(año_usuario):
    print(f"El año {año_usuario} es bisiesto.")
else:
    print(f"El año {año_usuario} no es bisiesto.")
