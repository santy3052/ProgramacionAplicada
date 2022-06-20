## 06- ESTRUCTURAS BASICAS
'''
las varaibles no son la única manera en la que se pueden almacentar las variables, en caso
que se desee almacenar dos o más datos se pueden utilizar estructuras que permiten esto
'''
# listas
'''
las listas tienen la siguiente sintaxis
variable = [valor1,valor2, ..., valorN]
estas pueden almacenar distintos tipos de datos incluso listas de manera que se pueden representar 
matrices como listas de listas 
'''
list_0 = [0,1,2,3,4,5,6,7,8,9]
list_1 = ['perro','gato','pajaro','cocodrilo','dinosaurio']
list_3 = [list_0,list_1]
# Para acceder a los datos de la lista se utilizan los indices de cada elemento
print(list_3[0][0])
#Se pueden tomar intervalos de datos
print(list_0[2:5])
print(list_0[7:])
print(list_0[-1])
print(list_0[-10])
# Si se exede el número de indices en cualquer dirección se arroja un error
#print(list_0[-15]) # IndexError: list index out of range

#Para acceder a una lista dentro de una lista se utilizan dos indices
print(list_3[1][3])
#Tuplas
'''
las tuplas son un tipo de datos que no pueden ser modificados una vez se han definido en el espacio 
al igual que las listas se pueden almacenar datos de independiente del tipo y se tienen funciones similares
en este caso la sintaxis es: 
variable = (valor1,valor2, ..., valorN)
'''
tuple_0 = (0,1,2,3,4,5,6)
#tuple_0[2] = 4 # TypeError: 'tuple' object does not support item assignment

# Diccionarios
'''
Los diccionarios son un tipo de estructura que tiene una llave que permite acceder a los valores asignados 
Diccionario = {'Llave': valor, 'llave2': valor, ...}
diccionario = dic(llave = valor, llave = valor, ...)
'''

dict_0 = dict(nombre = ['pepito','pepita'], edad = [21,22],clases = [['A1','A2'],['A2','A3']])
dict_1 = dict(nombre = ['pepito1','pepita2'], edad = [20,23],clases = [['A1','A2'],['A2','A3']])

print(dict_0['nombre'][0])
print(dict_0['nombre'])
print(dict_0['clases'][0])