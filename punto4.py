#Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.

print(" ")
print("Torres Olvera Gael")
print(" ")

#Solicitar al usuario que ingrese una cadena
cadena = input("Por favor, ingresa una cadena: ")

#Contar las letras mayúsculas
contador_mayusculas = sum(1 for letra in cadena if letra.isupper())

#Mostrar el resultado
print(f"La cadena tiene {contador_mayusculas} letras mayúsculas.")

