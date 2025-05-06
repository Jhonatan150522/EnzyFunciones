# 11. Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te
# devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además,
# recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login
# incremente este valor. Crear un programa principal donde se pida un nombre de usuario y una
# contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.
def Login(Usuario, contraseña):
    # Datos válidos
    UsuarioCorrecto = "usuario1"
    ContraseñaCorrecta = "asdasd"

    # Verificamos si el usuario y la contraseña coinciden
    return Usuario == UsuarioCorrecto and contraseña == ContraseñaCorrecta

# Programa principal
print("Tienes 3 intentos para hacer login.")

# Usamos un ciclo for con 3 intentos
for intento in range(1, 4):
    # Pedimos los datos al usuario
    usuario = input("Ingrese su nombre de usuario: ")
    clave = input("Ingrese su contraseña: ")

    # Verificamos si el login es correcto, llamando a la función
    if Login(usuario, clave):
        print("iniciando sesion...")
        # Salimos del ciclo si es correcto
        break 

    # Si el login no es correcto, mostramos un mensaje
    else:
        if intento < 3:
            print(f"datos incorrectos. Te queda(n) {3 - intento} intento(s).")
        else:
            print("acceso denegado.")




























