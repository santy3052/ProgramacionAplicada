## 16-EJERCICO 03 RECURSIÓN
'''
Los ejercicios son de caracter obligatorio, sin embargo no se les asignará una calificación, el objetivo de estos
es que ustedes practiquen y mejoren sus habilidades.
estos los deben subir de manera individual en su cuenta de Git
'''
'''
se les darán multiples funciones, así como la documentación correspondiente
 deben completar las tareas marcadas como TODO
'''
## DEMOSTRACIONES MATEMATICAS
# ejercicios tomados de: https://elvex.ugr.es/decsai/java/pdf/7D-Ejercicios.pdf

#TODO: Demuestre por inducción que, para todo n mayor o igual que 4, n!>2^n
N=int(input('ingrese su numero')) # se pide el numero
fact=1 # se define la variable para el factorial
if N!=0: # condicion para poder ejecutar el codigo
    for i in range(1,N+1): # se le da un rango a i para que al repetirse aumente su valor en 1 y cumpla la regla del factorial
        fact=fact*i #se añade el resultado a la variable
else:
    print('el factorial es 0') # si el numero ingresado es 0 se imprime este mensaje
pot=2**N # se hace la operacion de la potencia
if fact>pot:
    print(f'el numero {N} es mayor o igual a 4 y cumple la sentencia de: N!>2^N: {fact}>{pot}') #si el numero es mayor o igual se imprime el resultado

#TODO: Un granjero ha comprado una pareja de conejos para criarlos y luego venderlos.
#   Si la pareja de conejos produce una nueva pareja cada mes y la nueva pareja
#   tarda un mes más en ser también productiva, ¿cuántos pares de conejos podrá
#   poner a la venta el granjero al cabo de un año?
def conejos(n):
    if n== 0 or n==1: # se da la condicion para los dos primeros meses
        return 1
    return conejos(n-1)+conejos(n-2) # se da la operacion para los meses mayores a 1
n=int(input("coloque el numero del mes: (XX)")) # se pide al usuario la cantidad de meses a transcurrir
print(f'el numero de parejas que podra poner a la venta al cabo de {n}  meses seran {conejos(n)} parejas') # se da la cantidad de parejas para la venta
## Ejercicio objetos.
# TODO: 1. Cree un archivo, Taller donde llevará acabo el codigo principal
#       crear una lista de vehiculos que se encuentran en el taller en ese momento que tienen asociados: fecha de entrega, costo, modelo, año y dueño
#       crear una caja donde se almacena el dinero y se lleva registro de los movimientos
#       crear una lista de empleados que tienen asociado un nombre, cargo, salario, vehiculo y documento
#       Crear una lista de clientes que tienen asociado un nombre, vehiculo y documento

# TODO: 2 Ejecute sobre so codigo principal:
#       ingresar un vehiculo nuevo al taller (validar cupo)
#       Sacar un vehiculo del taller (se debe generar un pago por parte del cliente)
#       PAgar a los empleados (se debe hacer una reducción en el dinero de la caja)
#       Contrarar a una persona nueva
#       Despedir a una persona
#       Encontrar un vehiculo a partir de su dueño y determinar si está en el taller
# TODO: 3 Todas las funciones que implemente deben estar en un script distinto al principal y donde se definen sus clases
#       NOTA - (la UNICA exepción son las funciones que definen dentro de sus clases.)

