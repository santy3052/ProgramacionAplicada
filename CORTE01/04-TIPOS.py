## 04-TIPOS DE DATOS
'''
en la siguiente seccion revisaremno cuales son los distintos tipos de datos así como algunas formas de utilizarlos
'''
## Datos booleanos
'''
los datos booleanos represantan magnitudes binarias (solo pueden tomar dos valores)
y se utilizar para determinar si una condición o más condiciones se cumplen. 
'''
b_1 = True
b_0 = False
# Operadores lógicos
# OR
# se muestra el resultado del operador lógico OR

print(b_0 or b_0)
print(b_1 or b_0)
print(b_0 or b_1)
print(b_1 or b_1)
# AND
# se muestra el resultado del operador lógico AND
print('Resultadod del operador lógico AND')
print(b_0 and b_0)
print(b_1 and b_0)
print(b_0 and b_1)
print(b_1 and b_1)
# NOT
# Se muestra el resultado del operador NOT
print('Resultadod del operador lógico NOT')
print(not b_0)
print(not b_1)

## numericos
'''
las variables de tipo numerico se utilizan para representar cantidades
y pueden ser utilizadas con operaciones algebraicas
'''
s_0 = 130 # En este caso se tiene un número entero que se puede expresar en 8 bits o más
s_1 = 159.13 # se pueden expresar numeros fraccionarios (se determina el decimal con '.')
s_2 = float(136*10**7) # Los datos de tipo flotante se basan en expresiones algegraicas con exponenciales
                       # para almacenar números muy grandes
s_3 = 4 + 2j  # En el caso de los números complejos se utiliza un j para designar la parte imaginaria

print(type(s_0))
print(type(s_1))
print(type(s_2))
print(type(s_3))
# Operaciones con números
'''
los números son suceptibles a las operacioens algebraicas como lo son
Suma                +
multiplicación      *
división            /
resta               -
modulo (remanente)  %
'''
# la operación modulo, permite obtener el remamente de dos números
int_0 = 15
int_1 = 4

print (15%4)
print(4%15)
## Conversiones entre tipos de variables
'''
en muchos casos es necesario convertir un tipo de variable a otro, un ejemplo de otro es cuando se desea que 
el usuario ingrese un número mediante la función 'input' en este caso, se tiene siempre un string pero se 
puede convertir a un entero como se muestra a continuación, para trabajar con cadenas de caracteres se puede 
realizar la operación opuesta (de número a cadena de caracteres)
'''

print(type(input('ingrese un número: '))) # como se puede observar se tiene una cadena de caracteres

print(type(int(input('ingrese un número: ')))) # como se puede observar se tiene un entero

'''
int - para la conversión a enteros 
str- para la conversión a string 
'''