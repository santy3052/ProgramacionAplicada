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
def parconejos(n):
    if n== 0 or n==1: # se da la condicion para los dos primeros meses
        return 1
    return parconejos(n-1)+parconejos(n-2) # se da la operacion para los meses mayores a 1
n=int(input("coloque el numero del mes: (XX)")) # se pide al usuario la cantidad de meses a transcurrir
print(f'el numero de parejas que podra poner a la venta al cabo de {n}  meses seran {parconejos(n)} parejas') # se da la cantidad de parejas para la venta
## Ejercicio objetos.
# TODO: 1. Cree un archivo, Taller donde llevará acabo el codigo principal
#       crear una lista de vehiculos que se encuentran en el taller en ese momento que tienen asociados: fecha de entrega, costo, modelo, año y dueño
#       crear una caja donde se almacena el dinero y se lleva registro de los movimientos
#       crear una lista de empleados que tienen asociado un nombre, cargo, salario, vehiculo y documento
#       Crear una lista de clientes que tienen asociado un nombre, vehiculo y documento
class vehiculo ():
    def __init__(self,fde,cost,mod,año,dueño):
        self.fechaentrega=fde
        self.costo=cost
        self.modelo=mod
        self.año=año
        self.dueño=dueño

caja=50000

class empleados ():
    def __init__(self,nom,carg,sal,veh,doc):
        self.nombre=nom
        self.cargo=carg
        self.salario=sal
        self.vehiculo=veh
        self.documento=doc

class cliente ():
    def __init__(self,name,veh,doc):
        self.nombre=name
        self.vehiculo=veh
        self.documento=doc

v1=vehiculo('15-agosto',1000,'c1',2009,cl1.nombre)
v2=vehiculo('19-junio', 3000,'a2',2017,cl3.nombre)
v3=vehiculo('5-diciembre',4500,'b3',2022,cl2.nombre)
e1=empleados('Juan','gerente',5000,'a2',10504210)
e2=empleados('lucas','empleado',2000,'c2',10628492)
e3=empleados('Rodrigo','empleado',2500,'b2',10543619)
cl1=cliente('Juliana',v1,10528462)
cl2=cliente('Maria',v3,10524252)
cl3=cliente('Santiago',v2,10578259)

# TODO: 2 Ejecute sobre so codigo principal:
#       ingresar un vehiculo nuevo al taller (validar cupo)
#       Sacar un vehiculo del taller (se debe generar un pago por parte del cliente)
#       PAgar a los empleados (se debe hacer una reducción en el dinero de la caja)
#       Contrarar a una persona nueva
#       Despedir a una persona
#       Encontrar un vehiculo a partir de su dueño y determinar si está en el taller

v4=vehiculo('27-diciembre',1000,'a2',2020,cl4.nombre)
cl4=cliente('Simon',v4,10538471)
print('hay un nuevo vehiculo en el taller')
pago=1000

if pago >= v1.costo:
    caja+=pago
    print(' se hizo el pago y ',cl1.nombre, 'pudo sacar su vehiculo')

# TODO: 3 Todas las funciones que implemente deben estar en un script distinto al principal y donde se definen sus clases
#       NOTA - (la UNICA exepción son las funciones que definen dentro de sus clases.)
