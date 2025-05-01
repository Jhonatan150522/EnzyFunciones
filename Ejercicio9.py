# 9. Crear un programa que registre 50 números enteros y luego muestren los elementos que son
# múltiplos de 5, este se determina si con la fórmula de: Numero_ingresado_porteclado mod = 0.


# Se realiza la funcion
def mostrar_multiples_de_5():
# se relaiza una lista para poder almacenar los mnumeros
    Numeros = []
    #Se hace un ciclo for para los 50 numeros enteros
    print("Porfavor ingresa los 50  numeros enteros")
    for i in range(5):
        numero = int(input(f"Ingrese el numero {i + 1}: "))
        #Se guarda los numeros en la lista
        Numeros.append(numero)
    #Se muestran los numeros que son multiplos de 5
    print("Los numeros que son multiplos de 5 son: ")
    for numero in Numeros:
        if numero % 5 == 0:
            print (numero)
# Se llama la funcionn
mostrar_multiples_de_5()