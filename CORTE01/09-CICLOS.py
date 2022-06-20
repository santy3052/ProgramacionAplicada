## Ciclos for
'''
Un ciclo for permite dar recorridos definidos, es decir se conoce el punto de inicio y de parada, se parte de indices para definir el ciclo
no de condiciones booleanes
para definir in ciclo for
for variable in range N: #donde N es el valor maximo que se va a tomar
for elemnt in list: # donde elemt es cada uno de los elementos en la lista list
'''
list_0 = [0,1,2,3,4,12,6,7,8,9]
for inx in range(10):
    print (inx)

for num in list_0:
    print(num)

## Ciclos while
'''
en un ciclo while se parte de condiciones booleanas para terminar el ciclo o bien utilizando un break
en este caso de define como 
while condición: # donde la condición es un valor booleano 
while True: # Se define un ciclo infinito y en algún punto de la función se agrega un break para detener la función 
    break
'''
s_cont = 0
while True:
    print(s_cont)
    s_cont += 1
    if s_cont == 10:
        break

while s_cont < 10:
    print(s_cont)
    s_cont += 1

## TRY EXCEPT
'''
En algunos casos pueden ocurrir errores, que terminan de manera abrupta un código, por ese motivo puede ser útil 
manejar los distintos errores que se pueden presentar, para esto se utiliza la estructura try except 
'''

while True:
    str_No = input('ingrese un número entero: ')
    try :
        s_No = int(str_No) # esta funcion arroja un error si el valor no se puede convertir a un entero
    except:
        print('el valor ingresado no es un número entero, ingrese otro número')
        continue
    s_mod = s_No%2
    if s_mod == 0:
        print('es un númeor par')
    else:
        print('es un número impar')