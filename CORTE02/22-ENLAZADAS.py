## 22 - ESTRUCTURAS DE DATOS - LISTAS ENLAZADAS
'''
en los dos ejemplos vimos dos estructuas de datos que se comportan de manera distinta, en el primer caso (colas)
vimos un tipo de estructura llamado estructuras enlazadas, esto quiere decir que un dato tiene conocimiento de otro
y de esta manera se construye la estructura.
por otra parte en las pilas se observó que los datos son independientes y lo que se modifica es la estructura así
como la forma de acceder a estos
'''

#TODO: implentar una clase cola sin estructuras enlazadas
#TODO: implentar una clase pila haciendo uso de estructuras enlazadas

'''
ahora veremos otro tipo de estructura enlazada en la cual se tiene acceso a los datos anterior y siguiente.
'''

class lista (object):
    def __init__(self):
        self.anterior = []
        self.siguiente = []
        self.atributos = []

    def agregar_end (self,new):
        # se evalua el caso trivial (que se encuentre en la ultima posición)
        if self.siguiente == []:
            # Se realiza la asignación de datos
            self.siguiente = new
            # se modifica el dato siguiente de manera que el dato actual
            self.siguiente.anterior = self
        # para el caso no trivial
        else:
            self.siguiente.agregar_end(new)

    #TODO: crear una función que permita agregar un dato al inicio de la lista
    #TODO: crear una función que permita agregar un dato en cualquier posición de la lista
    #TODO: crear una función que permita eliminar un dato en cualquier posición de la lista
    #TODO: implementar una aplicación de su elección con las 3 estructuras vistas hasta el momento
    #   ¿que ventajas y desventas encuentra en cada una de ellas?