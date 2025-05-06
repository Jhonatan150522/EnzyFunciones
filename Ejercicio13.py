# # Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1  miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for  anidado.
#Se realizan las dos litas
# def superposicion ():

def superposicion (lista1, lista2):
#Se realizan las listas
  Lista1=[]
  Lista2=[]
  #Se añade un for para la lista 1
  Canti1=int(input("Digite la cantidad de la lista 1: "))
  for i in range(Canti1):
    X=int(input(f"Ingrese el numero{1 + i}: "))
    Lista1.append(X)
  #Se añade un for para la lista 2
  Canti2 =int(input("Digite la cantidad de la lista 2: "))
  for e in range(Canti2):
    X2=int(input(f"Ingrese eL numero{1 + e }:  "))
    Lista2.append(X2)
#Ahora se comparan las listas
  for item in Lista1:
    for item2 in Lista2:
      if item == item2:
        return True
  return False

Lista1=[]
Lista2=[]
#Se Muestra el resultado
print(superposicion(Lista1,Lista2))



