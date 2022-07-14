# NOTA: no les parece impresionante que como tal tenemos 18 clases (sin contar examenes) pero hasta
#el momento hay 30 archivos ... y me hacen falta 5 o 6 si no me equivoco

## 30 - GRAFICAS HACIENDO USO DE PYPLOT
'''
al igual que numpy pyplot es una librería de python pero en este caso esta nos permite realizar graficas de
funciones previamente creadas.
en el primer ejemplo, veremos graficas de liena simple principalenete de funciones matemáticas.
'''

# Importar librerías
import numpy as np
import matplotlib.pyplot as plt

# se crea una función seno
s_A = 10
s_F = 0.5
s_SRate = 150
v_TS = [0,10]

v_time = np.linspace(v_TS[0],v_TS[1],num= v_TS[1]*s_SRate)
v_sin = s_A * np.sin(v_time*s_F*np.pi)

# para la primera grafica simplemente se graficará la función anterior

#Se crea la figura que va a contener la imagen, esta funcion nos permite controlar distintos parametros de la figura
plt.figure()
# Esta función realiza la grafica como tal, es posible ajustar los parametros en esta función o despues
plt.plot(v_time,v_sin)
# a continuación se muestra la figura, dependiendo del IDE no es necesario pero para garantizar la compatibilidad
#es necesario incluir la siguiente linea de código
plt.show()

''' 
en caso que se deseen graficar multiples lineas sobre una misma figura, se puede hacer uso de las mismas funciones 
y el color se ajustará de manera automatica siguiendo una paleta por defecto como se muestra en el siguiente ejemplo
'''
s_F = 1
v_cos = s_A * np.cos(v_time*s_F*np.pi)
s_F = 2
v_sin2 = s_A*2 * np.cos(v_time*s_F*np.pi)

fig = plt.figure()
'''
Una de las funciones que resulta util es el uso de legentas para marcar cada una de las lineas utilizadas esto se 
construye a partir de labels 
'''
plt.plot(v_time,v_sin,v_time,v_cos,v_time,v_sin2)
# al hacer uso de legendas es necesario mantener el orden de las graficas.
plt.legend(['Seno1','Coseno','Seno2'])
# para marcar los ejes
plt.ylabel('Unidades (x)')
plt.xlabel('Tiempo (s)')
plt.show()

'''
entre otras funciones que se pueden realizar con esta librería es hacer multiples gráficas en una misma 
figura (subplot), así como cambiar el tamaño de los ejes
'''

#TODO: graficar cada uno de las lineas en un subplot distinto y ajustar los limites tanto en x como y para dejar
#   un marco de un 15% en cada dirección del punto más cercano

'''
esta librería no se limita a graficas lineales, se puede hace uso de la documentación para revisar los distintos 
elementos como se muestra a continuación 
https://matplotlib.org/stable/api/pyplot_summary.html
'''