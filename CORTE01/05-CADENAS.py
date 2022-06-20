## 05-CADENAS DE CARACTERES

## String
'''
Las cadenas de caracteres permiten almacenar información en un formato alfa numerico, y se pueden
procesar con distintas funciones nativas del sistema, en python se utiliza '' para designar una
cadena de caracteres
'''

str_0 = 'Casa' # no se pueden almacenar tanto mayusculas como minuzculas
str_1 = 'había una vez una iguana con una ruana de lana peinandose la melena junto al rio magdalena'
str_2 = 'HOLA MUNDO'
str_3 = 'haBíA. uNa. vEz'
# las string se pueden unir para formar una cadena más larga
print(str_0+str_1)
# capitalize, Permite colocar mayusculas en el primer elemento de un srtring
print(str_0.capitalize())
print(str_1.capitalize())
print(str_2.capitalize())
print(str_3.capitalize())
#lower, convierte todos los valores a minusculas
print(str_2.lower())
print(str_1.lower())
# upper  convierte todos los valores a mayusculas
print(str_2.upper())
print(str_1.upper())
# swapcase, convierte mayusculas en minusculas y minusculas en mayusculas
print(str_3.swapcase())
# len, retorna la longitud de un string
#  startswith() y endswith()  retorna un valor booleanos que determina si una cadena empieza o termina
# en un valor
# find() Encuentra la posición de un elemento en una cadena
#split() permite separar una cadena de acuerdo a espacios o un elemento en particular