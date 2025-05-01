# Diseñe un algoritmo que genere los 50 primeros números de la serie Fibonacci.
# Función para generar los primeros 50 números de la serie Fibonacci
def fibonacci(n):
    # Inicializar los dos primeros números de la serie Fibonacci
    a, b = 0, 1 # esto es igual a a = 0 y b = 1
    # Imprimir los primeros n números de la serie
    for _ in range(n): #se utiliza el coclo for ppara iterar n 
        print(a, end=" ")
        a, b = b, a + b  # Actualizar los valores de a y b

# Llamar a la función para generar los primeros 50 números de Fibonacci
fibonacci(50)
