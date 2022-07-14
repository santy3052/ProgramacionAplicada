#29-NUMPY
'''
Antes de iniciar a graficar es necesario revisar la manera de realizar operaciones matematicas haciendo uso de las
herramientas disponibles en el lenguaje de programación. Una de estas herramientas es la librería numpy la cual
brinda distintas facilidades para hacer operaciones matematicas y trabajar con vectores (listas que contienen
números de manera excusiva)
pueden conseguir la documentación de la librería en el siguiente enlace
https://numpy.org/
'''
# importar librería

# TODO: comentar la función de la siguiente linea de código
import numpy as np

a = np.arange(6)
print(a)
print(type(a))
# como se puede observar se tiene un objeto de tipo numpy.ndarray que no es mismo objeto nativo de python para listas
# Una de las funciones de numpy es que permite crear arreglos de 1 o 0 según se requiera
print(np.zeros(10))
# Se puede seleccionar la fomra que tendran estos vectores
print(np.ones([2,3]))

'''
ahora debemos introducir un concepto relevante para la construcción de funciones matemáticas, la frecuencia de 
muestreo, este valor nos indica cuantos datos se estan tomando en un instante de tiempo (normalmente en HZ o 
FPS para imagenes) este nos permite construir un vector de tiempo que se encuentre acorde al tiempo real de una señal
'''
# Construcción de un vector de tiempo con numpy
s_SRate = 150 # frecuencia de muestreo en Hz, en este caso se consideran 150 muestras por segundo
v_timeStamp = [0,10] # puntos de inicio y parada del vector de tiempo
v_time = np.linspace(v_timeStamp[0],v_timeStamp[1],num=v_timeStamp[1]*s_SRate)

# A partir de estos elementos podemos construir una función matematica que podemos graficar despues
s_Amplitude = 10 #Amplitud que se le dará a una función seno
s_Freq = 0.5 # frequencia que tendrá la función seno
v_sin = s_Amplitude*np.sin(v_time*s_Freq*np.pi)