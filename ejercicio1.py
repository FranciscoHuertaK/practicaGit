def tabla(numero):
    for x in range(1,11):
        print(f"{numero}X{x}={numero*x}")

def area_cuadrado(lado):
    print(f"El area es: {lado*lado}")

def operaciones(numero1,numero2,operacion):
    if operacion == 1:
        print(f"La suma de {numero1} mas {numero2} es igual a {numero1+numero2}.")
    elif operacion == 2:
        print(f"La resta de {numero1} menos {numero2} es igual a {numero1-numero2}.")
    elif operacion == 3:
        print(f"La multiplicacion de {numero1} por {numero2} es igual a {numero1*numero2}.")
    elif operacion == 4:
        print(f"La division de {numero1} entre {numero2} es igual a {numero1/numero2}.")

