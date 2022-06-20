## Funciones
'''
Las funciones permiten simplicar el código de manera que se pueden ejecutar una sección del código al llamar esta función
para esto se define de la siguiente forma
def nombre_de_la_función (parametros): # los parametos son el nombre de las variables que se van a utilizar en la función
    código
def nombre_de_la_función(nombre=valor,nombre=valor,...) # En este caso se definen valores predeterminados de manera que el
                                        usuario no necesita ingresar todos los valores
# Es posible conbinar las definición (tener unos parametros opcionales y otros obligatorios)
'''

# Se tiene una función que le permite sumar datos e eimprime el resultado, notar que esta función no retorna ningún valor
def f_suma(a,b):
    print(a+b)
# se tiene una función que retorna un valor
def f_sumaR (a,b):
    return a+b
# se meustra una función donde todos los parametros son opcionales
def f_diHola (nombre='Pepito'):
    print ('hola ' + nombre)
# función donde se tienen parametros opcionales y obligatorios

def f_diHola2(nombre,edad ='30'):
    print ('hola ' + nombre + ' tienes ' + edad + 'años')

## Se laman las funciones anteriores
f_suma(2,3)
print(f_sumaR(4,5))
f_diHola()
f_diHola('dinosaurio')
f_diHola2('dinosaurio')
f_diHola2(nombre = 'dinosaurio',edad = '15')