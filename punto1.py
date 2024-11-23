#Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande

print(" ")
print("Torres Olvera Gael")
print(" ")

def max_in_list():
    #Solicitar al usuario que ingrese números separados por espacios
    user_input = input("Ingrese una lista de números separados por espacios: ")
    
    #Convertir la entrada en una lista de números
    number_list = [float(num) for num in user_input.split()]
    
    #Devolver el número más grande de la lista
    return max(number_list)

#Llamar a la función y mostrar el resultado
resultado = max_in_list()
print("El número más grande es:", resultado)