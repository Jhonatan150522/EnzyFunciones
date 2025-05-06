# Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente
# todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y
# multip([1,2,3,4]) debería devolver 24.

#Se escribe la funcion sum() y la funcion multip()
def Multip ():
#Se hace la lista respectivamente
  ListaNumero = []
#Se le pide la lista de la cantidad de veces que el usuario 
  Canti= int(input("Ingrese la cantidad de numeros que va a ingresar: "))
#Se agrega un for para poder Mostrar las cantidad que el usuario ingreso 
  for i  in range (Canti):
    NI= int(input(f"Ingrese el numero {1 +i}: "))#Le mustra al usuario para que ingrese los numeros 
    ListaNumero.append(NI)#Se agrega a la lista
    X= 1 # Se hace esta variable para que siempre empiece en uno 
#Se realiza un for para poder realizar las multiplicaciones 
  for NI in ListaNumero:
    X *= NI
# Se muestra el resultado
  print ("Los numeros son:",ListaNumero)
  print(f"El resultado es; {X}")
# Se llama la funcion
Multip()


#Se hace lo mismo,
def Suma ():
  ListaNumero = []
#Se le pide la lista de la cantidad de veces que el usuario 
  Canti= int(input("Ingrese la cantidad de numeros que va a ingresar: "))
#Se agrega un for para poder Mostrar las cantidad que el usuario ingreso 
  for i  in range (Canti):
    NI= int(input(f"Ingrese el numero {1 +i}: "))#Le mustra al usuario para que ingrese los numeros 
    ListaNumero.append(NI)#Se agrega a la lista
    X= 0 # Se hace esta variable para que siempre empiece en uno 
#Se realiza un for para poder realizar las multiplicaciones 
  for NI in ListaNumero:
    X += NI
# Se muestra el resultado
  print ("Los numeros son:",ListaNumero)
  print(f"El resultado es; {X}")
# Se llama la funcion
#Se llama la funcion 
Suma()
