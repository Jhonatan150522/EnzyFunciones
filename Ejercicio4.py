# Lorena organiza una fiesta en la cual una computadora controla el ingreso mediante 5 claves. Si
# se ingresa al menos una clave incorrecta esta imprimirá "TE EQUIVOCASTE DE FIESTA" y no
# permitirá el ingreso. Si las 5 claves son correctas imprimirá "BIENVENIDO A LA FIESTA"
# Las Claves son:
# 1: "TIENES"
# 2: "QUE SER"
# 3: "INVITADO"
# 4: "PARA"
# 5: "INGRESAR"
#Se realiza una lisata con las palabras correctas
ClavesCorrectas=["TIENES", "QUE SER", "INVITADO", "PARA", "INGRESAR"]

#Se Le dice al usuario para poder ingresar a la fiesta que digite la clave
print("Para poder ingresar a la fiesta ingrese de manera correcta la clave")
#Se realiza la funcion
def PedirClave ():
    todoBien = True
#Se usa For para poder repetir las 5 claves 
    for i in range (5):
        Clave = input(f"Digite la Clave {i+1}: ").strip().upper()
        if Clave != ClavesCorrectas[i]:
            todoBien = False
            break
    return todoBien
# Se llama la funcion y se verifica si toso esta bien
if PedirClave():
    print("--"*50)
    print("Bienvenido a la fiesta")
    print("--"*50)
else:
    print("te equivocaste de clave")