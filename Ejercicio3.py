# 3. Calcular el sueldo que le corresponde al trabajador de una empresa que cobra $14.400.000
# anual, el programa debe realizar los cálculos en función de los siguientes criterios:
# a. Si lleva más de 10 años en la empresa se le aplica un aumento del 10%.
# b. Si lleva menos de 10 años, pero más que 5 se le aplica un aumento del 7%.
# c. Si lleva menos de 5 años, pero más que 3 se le aplica un aumento del 5%.
# d. Si lleva menos de 3 años se le aplica un aumento del 3%.
#  Se declara la funcion 
def CalcularSueldo(Time):
    # Cada trabajador cuenta con un salario mensual de 1.200.000
    SueldoBase= 1200000
    # Mas de 10 años en la empresa = %10
    if Time > 10:
        SueldoT= (SueldoBase*0.10)/100
        print("*"*80)
        print(f"Su aumento es del 10% en total con el amento es: {round(SueldoT,3)}")
        print("*"*80)
    # Menos de 10 años en la empresa = 7%
    elif Time < 7:
        SueldoT= (SueldoBase*0.07)/100
        print("*"*80)
        print(f"Su aumento es del 7% en total con el aumento es: {round(SueldoT,3)}")
        print("*"*80)
    # Menos de 5 años pero mas que 3 años = 5%
    elif Time < 5 and Time >= 3:
        SueldoT= (SueldoBase*0.5)/100
        print("*"*80)
        print(f"Su aumento es del 5% en total con el aumento es: {round(SueldoT,3)}")
        print("*"*80)
    # Menos de 3 años aumento de 3%
    elif Time < 3:
        SueldoT= (SueldoBase*0.3)/100
        print("*"*80)
        print(f"Su aumento es del 3% en total con el aumento es: {round(SueldoT,3)}")
        print("*"*80)

    return print

Time = int(input("Digite el tiempo que lleva en nuestro Tiempo:"))
Resultado = CalcularSueldo(Time)
print(Resultado)