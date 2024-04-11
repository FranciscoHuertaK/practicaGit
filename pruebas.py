import ejercicio1

#Probar la tabla
numero = int(input("Que tabla quieres?"))
ejercicio1.tabla(numero)

#Probar la funcion de area del cuadrado
lado = int(input("Dame la longitud de un lado del cuadrado: "))
ejercicio1.area_cuadrado(lado)

#Probar la funcion de operaciones
numero1 = int(input("Dame el primer numero: "))
numero2 = int(input("Dame el segundo numero: "))
operacion = int(input("¿Que operacion deseas realizar? \n 1.Suma \n 2.Resta \n 3.Multiplicacion \n 4.Division \n"))
ejercicio1.operaciones(numero1,numero2,operacion)