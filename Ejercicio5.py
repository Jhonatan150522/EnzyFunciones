# 5. Algoritmo Calcular la factorial de un número N.
def calcular_factorial(N):
    factorial = 1  # Inicializamos la variable para almacenar el resultado
    for i in range(1, N + 1):  # Iteramos desde 1 hasta N
        factorial *= i  # Multiplicamos factorial por i en cada paso
    return factorial  # Devolvemos el resultado final

# Solicitamos al usuario que ingrese el número N
numero = int(input("Introduce un número para calcular su factorial: "))
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es: {resultado}")
