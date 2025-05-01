# Construya los algoritmos que permitan calcular las siguientes series con un valor de N ingresado
# desde teclado:
# • 1
# 2 + 22 + 32+...N2

# tal que N es positivo

# • 1
# 1 + 22 + 33+...Nn

# tal que N es positivo


def calcular_serie_1(N):
    suma = 0  # Inicializamos la variable para almacenar la suma
    for i in range(1, N + 1):  # Iteramos desde 1 hasta N
        suma += i**2  # Sumamos el cuadrado de cada número
    return suma  # Devolvemos la suma total

# Solicitamos al usuario que ingrese el número N
numero = int(input("Introduce un número N para la serie 1 (1^2 + 2^2 + 3^2 + ... + N^2): "))
resultado = calcular_serie_1(numero)
print(f"La suma de la serie 1 es: {resultado}")
