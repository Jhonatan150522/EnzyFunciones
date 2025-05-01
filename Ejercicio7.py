# Diseñar un pseudocódigo que calcule el promedio ponderado para alumno del ITT. El cálculo se
# hace de la siguiente forma: Se multiplica cada calificación por los créditos de cada materia
# El resultado anterior se suma con los resultados de todas las materias, por separado se suman
# los créditos de cada materia y finalmente se divide la suma de todas las materias por sus
# respectivos créditos, entre la suma de todos los créditos. (materias: Fundamentos, BD y ética).

# Definir las calificaciones y los créditos de las materias
# Estas son las calificaciones obtenidas en cada materia y los créditos asignados a cada una
calificacion_fundamentos = 90  # Calificación obtenida en Fundamentos
creditos_fundamentos = 5       # Créditos asignados a la materia Fundamentos

calificacion_bd = 80           # Calificación obtenida en BD (Base de Datos)
creditos_bd = 4               # Créditos asignados a la materia BD

calificacion_etica = 85        # Calificación obtenida en Ética
creditos_etica = 3            # Créditos asignados a la materia Ética

# Calcular la suma ponderada
# Se multiplica cada calificación por los créditos de la materia
# Luego, se suman los resultados de todas las materias
suma_ponderada = (calificacion_fundamentos * creditos_fundamentos) + \
                 (calificacion_bd * creditos_bd) + \
                 (calificacion_etica * creditos_etica)

# Calcular la suma de los créditos
# Sumamos todos los créditos de las materias
suma_creditos = creditos_fundamentos + creditos_bd + creditos_etica

# Calcular el promedio ponderado
# El promedio ponderado se obtiene dividiendo la suma ponderada entre la suma total de los créditos
promedio_ponderado = suma_ponderada / suma_creditos

# Mostrar el resultado
# Se imprime el promedio ponderado con dos dos decimales 
print(f"El promedio ponderado es: {promedio_ponderado:.2f}")
