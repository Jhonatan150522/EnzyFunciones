# 1. Que calcule el gasto de agua en una vivienda dado el número de litros gastados, siendo el
# sistema de cobro:
# • La cuota fija mensual es de 600 pesos
# • Los primeros 50 litros son gratis (opción 1)
# • Mayor de 50 y 200 litros se cobra el litro a 1000 pesos (opción 2)
# • Mayor de 200 litros se cobra el litro a 3000 pesos (opción 3)

# #se define la funcion con su parametro 
def calcular_gasto_agua(litros):
    cuota_fija = 600 # esta es una cuota fija 
    total = cuota_fija # se le declara otra variable con el valor determinado que son los 600
#Se declaran la condicional if para realizar las operaciones 
    # Opción 1: hasta 50 litros

    if litros <= 50:
        total = cuota_fija

    # Opción 2: entre 51 y 200 litros
    if litros > 50 and litros <= 200:
        total = cuota_fija + (litros - 50) * 1000

    # Opción 3: más de 200 litros
    if litros > 200:
        total = cuota_fija + (150 * 1000) + (litros - 200) * 3000
# se retorna 
    return total
# Se le pregunta al usuario los litros consumidos (es el parametro de la funcion)
litros = int(input("Ingrese el número de litros consumidos: "))
# Se llama la funcion 
total_a_pagar = calcular_gasto_agua(litros)
# Se da la respuesta 
print("El total a pagar es:", total_a_pagar, "pesos")
