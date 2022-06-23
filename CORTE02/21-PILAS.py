# 21 -  ESTRUCTURAS DE DATOS - PILAS
'''
Otra de las estructuras que veremos son las pilas, en este caso, el ultimo dato en ser agregado es el primero en salir
'''

## definición de la clase
class pila (object):
    def __init__(self):
        self.items = []

    def add (self,new):
        self.items.append(new)

    def remove(self):
        self.items.pop()

    # TODO: realizar una función que permita validar si la estructura está vacia
    # TODO: realizer una función que permita validar el valor de cualquier elemetno en la estructura