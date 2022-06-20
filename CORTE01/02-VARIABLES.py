## 02 - MANEJO DE VARIABLES EN PYTHON
'''
En la siguiente sección revisaremos los conceptos de variables, que son y como se utilizan
'''
## Definición de variables
# ¿qué es una variable?
'''
Una variable permite alocar un espacio en memoria para guardar un valor especifico de interes
'''
a = 1
b = 2
'''
al almacenar estos valores en una variable, permite llamar estos sin la necesidad de declarar el valor contenido en 
la variable 
'''
c = a + b
print (c)
'''
En este caso se toman una operación entre a y b y se almacena en c de manera que esta pueda ser utilizada. 
Para definir una variable se utiliza el operador "=" el cual asigna a la variable de la izquierda el valor 
del lado derecho. es posible realizar asignaciones multiples con un mismo operador. 
por otra parte se puede sobreescribir una varible como se muenstra en el ejemplo siguiente 
'''

d = 'Hola mundo'
print (d)
d = 30
print(d)

'''
en este caso se puede observar como la misma variable "d" cambia de valor 
Por convención cuando se desean valores invariantes en el tiempo se utilizan letras en mayusculas.
'''
## Print
'''
en los ejemplos anteriores se utilizó la función print, esta permite imprir en pantalla el valor asignado a una 
variable, o un valor que se tenga dentro de esta
'''
print("Hola")
print(70)
a = 10
print (a)

## Asignaciones
'''
Como se vió anteriormetne el operador "=" permite asignar un valor a una variable sin embargo existen distintos 
operadores
    1. += Asigna el valor de la izquierda más el de la derecha
    2. -= asigna el valor de la izquierda menos el de la derecha 
    3. *= asigna el valor de la izquierda por el de la derecha 
    4. /= asigna el valor de la izquierda dividido por el de la derecha
    5. %= asigna el modulo de la izquierda contra el de la derecha 
NOTA: el modulo corresponde al residuo de la división 
'''

# +=
a = 10
print(a)
a += 1
print(a)
b = 5
a += b
print(a)

# -=

a = 4
a -= 8
print(a)

# *=

a*=b
print(a)
print (b) # como vemos la asignación no afecta el valor de la derecha.

# /=

a /= b
print(a)

# %=

a = 5
a %= 5
print(a)
a %= 3
print(a)
