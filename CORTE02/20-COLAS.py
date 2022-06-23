# 20 -  ESTRUCTURAS DE DATOS - COLAS
'''
Hasta ahora hemos visto estructuras de datos basicas, (listas tuplas diccionario)
a continuación veremos estructuras un poco más complejas, en estos casos tendrémos listas enlazadas, es decir
un dato contiene el dato siguiente.

la primera estructura que veremos son las colas.
estas estructuras indican que el primer elemento que llega es el primero en ser atendido
'''

# NOTA LOS CÓDIGOS REALIZADOS PARA LAS ESTRUCTURAS SON MÁS DE CARACTER EXPLICATIVO LA IMPLEMENTACIÓN NO ES LA FORMA
# EFICIENTE (NI CORRECTA) DE HACERLO PERO SIRVE PARA EXPLICAR


## Definición de la clase
class cola(object): # Se define la clase que corresponde a los datos en la cola
    # función de inicialización
    def __init__(self):
        # como parametro valores importantes se tiene el dato siguiente en la cola
        self.siguiente = []
        # adicionalmente se tienen los demás atributos del objeto
        self.atributos = []

    '''
    en este caso, es necesario implementar algunas funciones que nos permiten modificar la cola, principalmente 
    una función para agregar y otra para eliminar datos 
    '''
    def agregar (self,new):
        '''
        funcióin para agregar un dato al final de la cola
        :param new: elemento a agregar
        :return: # no se tiene un return, se está modificando el objeto como tal
        '''
        # Condición final -> se esta en el ultimo elemento de la cola
        if self.siguiente == []:
            self.siguiente = new
        else:
            # en caso que se intenta agregar en siguiente elemento de la lista
            self.siguiente.agregar(new)

    def remove (self):
        '''
        función para eliminar el ultimo objeto de la cola
        :return:
        '''
        '''
        en este caso, como no tenemos una forma de eliminar el objeto actual, debemos revisar el objeto siguiente 
        '''
        next  = self.siguiente
        if next.siguiente == []:
            self.siguiente = []
        else:
            self.siguiente.remove()

# TODO: realizar un código que permita eliminar cualquier elemento de la cola
# TODO: realizar un código que permita eliminar un dato cualquiera y reemplazarlo por otro elemento dado por parametro
# TODO: realizar una función que permita validar si la estructura está vacia
# TODO: realizer una función que permita validar el valor de cualquier elemetno en la estructura