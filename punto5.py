#Construir un pequeño programa que convierta números binarios en enteros.

print(" ")
print("Torres Olvera Gael")
print(" ")

def binario_a_entero(binario):
    #Convertir el número binario (como cadena) a entero
    return int(binario, 2)

#Solicitar al usuario que ingrese un número binario
numero_binario = input("Introduce un número binario: ")

#Convertir y mostrar el resultado
resultado = binario_a_entero(numero_binario)
print(f"El número binario {numero_binario} en entero es: {resultado}")