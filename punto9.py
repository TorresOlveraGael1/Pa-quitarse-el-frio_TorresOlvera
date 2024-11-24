#Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Definir la función contar_vocales
def contar_vocales(palabra):
    #Definir un diccionario para almacenar el conteo de cada vocal
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    #Recorrer cada letra de la palabra
    for letra in palabra.lower():  #Convertimos la palabra a minúsculas para contar sin importar mayúsculas
        if letra in vocales:  #Si la letra es una vocal, aumentamos el contador correspondiente
            vocales[letra] += 1

    #Imprimir el resultado
    for vocal, cantidad in vocales.items():
        print(f"La letra '{vocal}' aparece {cantidad} veces.")

#Solicitar al usuario que ingrese una palabra
palabra_usuario = input("Ingresa una palabra para contar las vocales: ")

#Llamar a la función con la palabra ingresada
contar_vocales(palabra_usuario)
