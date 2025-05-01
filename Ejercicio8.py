# 8. Diseñe un algoritmo que determine el resultado de la elección del representante estudiantil de la
# universidad X, para ello se presentaron tres candidatos A, B, y C.
# • Para ganar la elección se debe obtener como mínimo el 51%.
# • En caso que no haya un ganador se repite la elección en una segunda vuelta.
# • Van a la segunda vuelta los dos candidatos que obtengan la más alta votación.
# • Se anula la elección en caso de producirse un empate doble por el segundo lugar o un
# empate triple.
# Función para leer los votos de los candidatos
def leer_votos(candidato):
    return int(input(f"Ingrese el número de votos para {candidato}: "))

# Ingresar los votos de los tres candidatos
votos_A = leer_votos("Candidato A")
votos_B = leer_votos("Candidato B")
votos_C = leer_votos("Candidato C")

# Calcular el total de votos
total_votos = votos_A + votos_B + votos_C

# Calcular el porcentaje de votos para cada candidato
porcentaje_A = (votos_A / total_votos) * 100
porcentaje_B = (votos_B / total_votos) * 100
porcentaje_C = (votos_C / total_votos) * 100

# Verificar si algún candidato ha ganado con el 51% o más
if porcentaje_A >= 51:
    print("El ganador es el Candidato A")
elif porcentaje_B >= 51:
    print("El ganador es el Candidato B")
elif porcentaje_C >= 51:
    print("El ganador es el Candidato C")
else:
    # No hay un ganador, verificar si hay empate doble o triple
    if votos_A == votos_B == votos_C:
        print("La elección se anula por empate triple")
    elif votos_A == votos_B and votos_A > votos_C:
        print("Segunda vuelta: Candidatos A y B")
    elif votos_A == votos_C and votos_A > votos_B:
        print("Segunda vuelta: Candidatos A y C")
    elif votos_B == votos_C and votos_B > votos_A:
        print("Segunda vuelta: Candidatos B y C")
    else:
        print("Segunda vuelta: Candidatos con mayor votación")
