#Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n cairacteres.

print(" ")
print("Torres Olvera Gael")
print(" ")

def filtrar_palabras(lista_palabras, n):
    #Filtramos las palabras que tienen más de n caracteres
    return [palabra for palabra in lista_palabras if len(palabra) > n]

if __name__ == "__main__":
    #Pedir al usuario que ingrese una lista de palabras
    palabras = input("Introduce una lista de palabras separadas por espacios: ").split()
    
    #Pedir al usuario que ingrese un número entero
    n = int(input("Introduce el número de caracteres: "))
    
    #Filtrar las palabras
    resultado = filtrar_palabras(palabras, n)
    
    #Mostrar el resultado
    print("Palabras con más de", n, "caracteres:", resultado)