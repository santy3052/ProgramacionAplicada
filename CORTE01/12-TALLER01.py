## 12-TALLER 01
'''
El presente taller tiene como objetivo evaluar las habilidades adquiridas hasta el momento a lo largo del curso,
así como repasar los conceptos e introducir nuevas herramientas.
'''
# Recordatorio, el archivo lo deben subir a su repositorio en la fecha indicada.
## 1. Persistencia (1.0)
l_paises = ['Colombia','Mexico','Turquía','Polonia','serbia','dinamarca','holada','Alemania']
#TODO: escriba un programa que le permina escribir de manera automatica los nombres de estos paises en un archivo txt
#NOTA: todos los nombres deben tener una mayuscula al comienzo
#       el archivo se ecuentra en formato csv
SOLUCION 1    
nombre_archivo = 'programar.txt'  #se genera el nombre del archivo formato txt
with open(nombre_archivo, 'w',encoding='utf_8') as archivo:  # se usa with para genera la apertura del archivo, se usa el modo 'w' para escribir en él y se usa el encoding con el fin de poder generar caracteres especiales 
    archivo.write("l_paises = ['Colombia','Mexico','Turquía','Polonia','serbia','dinamarca','holada','Alemania']")  # se genera el mensaje dentro del archivo con el .write()
## 2. Lectura de archivos (1.0)
#TODO: escriba un programa que le permita leer e imprimir el archivo generado anteriormente
with open('programar.txt') as archivo:      # se llama al archvo generado y guardado anteriormente (en este caso en la misma carpeta)
    contenido = archivo.read()      # se determina una variable para contener la informacion del archvo pero en modo lectura con el .read()
    print(contenido)        #se imprime la variable del modo lectura

## 3. números binario (1.5)
def f_calBin (s_num):
    '''
    Calculadora que permite encontrar la representación en binario de un número entero o decimal que ingresa por parametro
    :param s_num: número que se desea convertir a binario int o float
    :return: valor número en binario
    '''
    #TODO: escribir la sección del codigo para las conversiones
    #NOTA: puede hacer uso de tantas funciones como necesite (diseñadas por el estudiante)
    s_bin = 0 #deben asignal el valor binario en esta variable
    return s_bin

#Test

assert f_calBin (1) == 1
assert f_calBin (4) == 100
assert f_calBin (10) == 1010
assert f_calBin (1.25) == 1.01

## 4. Valores estadisticos (1.5)
import numpy as np
def f_stat (l_valores):
    '''
    función que toma una lista de valores y retorna el promedio, la mediana y la desviación estandar
    :param l_valores: lista con los valores a utilizar
    :return:
    '''
    s_mean, s_median, s_STD = 0,0,0
    #TODO: realizar las modificaciones necesarias a partir de esta sección
    return s_mean,s_median,s_STD

## 5. BONO (0.5)
#TODO: realizar la verificación del punto aterior haciendo uso de la función assert (pytest)

