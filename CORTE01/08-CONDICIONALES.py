## 08-CONDICIONALES
'''
en la siguiente sección se revisaran los condicionales así como la sintaxis de estos.
'''
## Condicionales if
'''
una operación if permite evaluar condiciones booleanas, de manera que se ejecuta una sección del código solo si se cumplen las condiciones
'''
var_0 = 10
var_1 = 10
var_2 = 5
str_0 = 'pepito'
str_1 = 'pepita'
str_2 = 'Pepito'

if var_0 == var_1:
    print('las variables son iguales')
# Se tiene la función else donde se ejecuta el código si no se cumplen las condiciones anteriores
if var_0 == var_2:
    print('las variables son iguales')
else:
    print('las variables son distintas')
# Se tiene la función elif en este caso se tiene una segunda que solo se valida si los valores anteriores son False
if str_0 == str_2:
    print('las variables son iguales')
elif str_0 == str_1:
    print('las variables son iguales')
else:
    print('las variables no son iguales')

'''
en este caso las condiciones se evaluan de manera secuencial por lo tanto es posible que una condición nunca 
sea evaluada como se muestra en el siguiente ejemplo

¿qué condición no es evaluada?
'''
s_no = 10
if s_no > 10:
    print('Condión 1')
elif s_no > 0:
    print('Condición 2')
elif s_no > 4:
    print('condición 3')
else:
    print ('condición 4')