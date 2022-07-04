# 23- ESTRUCTURAS DE DATOS - ARBOLES

'''
hasta el momento todas las estructuras de datos vistas son de caracter linea, sin embargo esto no es una cocndicón
estricta, los arboles son estructuras de datos que enlazan a dos o más datos de manera ordenada lo que facilita
buscar elemento dentro de esta.

en este caso no centraremos unicamente en los arboles binarios (qué tienen soloamente 2 ramas en cada nodo) ya que
el estos se pueden convertir en arboles con n ramas y viceversa.
'''

## Definición de la clase

class arbol (object):
    def __init__(self,valor):
        self.mayor = []
        self.menor = []
        self.valor = valor
        '''
        en este caso se ordenan los datos de manera que a un lado del arbol se tienen todos los datos mayores y del 
        otro todos los datos menores, esta estructura reduce el número de comparaciones necesarias para encontrar un 
        dato, en este caso, con cada iteración se descarta la mitad de los datos 
        
        sin embargo, por tratarse de una estructura ordenada es necesario agregar los datos en un orden específico 
        '''

    def agregar(self,new):
        s_val = self.valor
        if s_val < new:
            if self.menor == []:
                self.menor.valor = new
            else :
                self.menor.agregar(new)
        else:
            if self.mayor == []:
                self.mayor.valor = new
            else:
                self.mayor.agregar(new)
    '''
    en este caso se tiene que validar la posición en la que se va a agregar el elemento nuevo y despues verificar si 
    este se encuentra vacio o no. 
    '''

    #TODO: REALIZAR UNA implementación que permita buscar un dato en una estructura de un arbol
    