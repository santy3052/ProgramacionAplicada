'''
Taller 02
# Calculadora
1. realice una función f_suma(N1,N2) que realice la suma entre dos números
2. realice una función f_resta(N1 = valor , N2 = valor) que realice la resta entre dos números, debe
3. realice una función f_calculadora(N1,N2,signo) que reciba dos números y realice la operación del signo (suma o resta)
4. pruebe su función y determine bajo que condiciones falla
# Maximos y minimos
1. realice una función f_max(list) que retorne el valor maximo de una lista (debe hacer uso de un ciclo while)
2. realice una función f_min(list) que retorne el valor minimo de una lista (lo debe realizar con un cico for)
3. realice una función f_minORmax(list,op = 'max') que implemente las dos funciones anteriores (op = max o min)
4. determine cual de las dos funciones (f_max o f_min) es más rapida (puebe con una lista de al menos 1000000 de datos)
# CSV
1. realice una función f_csv2list('string') que convierta un archivo separado por comas en una lista de elementos
2. pruebe su función con la cadena '2,3,4,5,6,7,8,9,0,hola'
NOTA: todas las funciones deben retornar el resultado de su operación
 '''
## Solución:
# f_suma
def f_suma (n1,n2):
    return (n1+n2)
#f_resta
def f_resta (n1 = 10, n2 = 7):
    return (n1-n2)
# f_calc
def f_calc (n1,n2,op):
    if op == '+':
        return(f_suma(n1,n2))
    else:
        return (f_resta(n1,n2))
# prueba de las funciones
print(f_suma(2,3))
print(f_resta())
print(f_resta(4,3))
print(f_calc(2,3,op='-'))
print(f_calc(2,3,op='+'))

#f_max
def f_max(list_0):
    s_max = list_0[0]
    cont = 1
    while cont < len(list_0):
        s_CurrElem = list_0[cont]
        if s_max < s_CurrElem:
            s_max = s_CurrElem
        cont += 1
    return s_max

def f_min(list_0):
    s_min = list_0[0]
    for elem in list_0[1:]:
        if s_min > elem:
            s_min = elem
    return s_min

def f_minORmax(list_0,op = 'max'):
    if op == 'max':
        return (f_max(list_0))
    else:
        return (f_min(list_0))

# prueba de las funciones
list_0 = [10, 20, 30, 50, 55, 44, 39, 12, 15, 10]
print(f_max(list_0))
print(f_min(list_0))
print(f_minORmax(list_0,'max'),'max')
print(f_minORmax(list_0,'min'),'min')
print(f_minORmax(list_0))

# tiempo
import random
import time
randomlist = random.sample(range(10, 200000), 100000)

t_init = time.time()
f_min(randomlist)
t_delta1= t_init - time.time()
print('timepo f_min' + str(t_delta1))

t_init = time.time()
f_max(randomlist)
t_delta1= t_init - time.time()

print('timepo f_max' + str(t_delta1))

# separación de cadenas de caracteres
def f_csv2list(string_0):
    return string_0.split(',')

# prueba
string_0 = '2,3,4,5,6,7,8,9,0,hola'
print(f_csv2list(string_0))

