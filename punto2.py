#Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

print(" ")
print("Torres Olvera Gael")
print(" ")

def mas_larga(lista_palabras):
    if not lista_palabras:  #Verifica si la lista está vacía
        return None
    palabra_larga = max(lista_palabras, key=len)  #Encuentra la palabra más larga
    return palabra_larga

#Ejemplo de uso
palabras = input("Introduce una lista de palabras separadas por espacios: ").split()
resultado = mas_larga(palabras)
print("La palabra más larga es:", resultado)