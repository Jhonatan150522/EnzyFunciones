# Realizar el siguiente juego: Piedra, papel o tijeras Este es un juego muy antiguo en el que
# intervienen dos personas. Cada jugador hace su elección entre las tres alternativas existentes
# (piedra, papel o tijeras) y el ganador se determina atendiendo a las siguientes reglas:
# • La piedra gana a las tijeras (puede golpearlas hasta romperlas).
# • Las tijeras ganan al papel (pueden cortarlo).
# • El papel gana a la piedra (puede envolverla).
# • Si las dos elecciones son la misma se produce un empate.

#Se realiza la funcion con sus parametros
def piedraPapelTijeras (Op1,Op2,Nom1,Nom2):
    if Op1 == 1 and Op2 == 2:
        Resultado= f"el ganador es {Nom2}"
        return Resultado
    elif Op1 == 1 and Op2 == 3:
        Resultado =f"el ganador es {Nom1}"
        return Resultado
    elif Op1 == 2 and Op2 == 1:
        Resultado= f"El ganador es {Nom1} "
        return Resultado
    elif Op1 == 2 and Op2 == 3:
        Resultado= f"el ganador es {Nom2}"
        return Resultado
    elif Op1 == 3 and Op2 == 1:
        Resultado= f"el ganador es {Nom1}"
        return Resultado
    elif Op1 == 3 and Op2 == 2:
        Resultado= f"el ganador es {Nom1}"
        return Resultado
    elif Op1 == Op2:
        Resultado= f"Es un empate"
        return Resultado

        
Nom1 = input("Ingrese su nombre (Jugador 1): ")
Nom2 = input("Ingrese su nombre (Jugador 2): ")
print ("Elige una opción",
    "1. Piedra",
    "2. Papel",
    "3. Tijera")
Op1 =int(input (f"Ingrese tu opcion Jugador {Nom1}: "))
Op2 =int(input (f"Ingrese tu opcion Jugador {Nom2}: "))
#Se llama la funcion 
# Resultado = piedraPapelTijeras(Op1,Op2,Nom1,Nom2)
total = piedraPapelTijeras(Op1,Op2,Nom1,Nom2)
print(total)