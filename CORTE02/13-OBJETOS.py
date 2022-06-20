#13-INTRODUCCIÓN A OBJETOS
'''
En la siguiente sección se realizará una introducción a los objetos en programación.
Un objeto es un elemento en el programa que cumple con un rol o una función especifica a lo largo de este.
para que un objeto sea de utilidad, este debe contar con distintas caracteristicas.
    atributos = los valores o caracteristicas que definen el objeto
    métodos = los las distintas funciones que se pueden implentar sobre un objeto
Una de las grandes ventajas de los objetos es que simplifican el código y facilitan su lectura.
Python así como muchos otros son lenguajes de programación orientados a objetos por lo que cada elemento de
este lenguaje es representado por un objeto, y las multiples librerías son implementadas de la misma manera.
'''
## Definición de una clase
'''
para implementar un objeto es necesario finir una clase, esta indica cuales son los atributos y métodos qué tendrá 
el objeto despues de ser definido en el código
'''
# para definir una clase se utiliza la palabra reservada del lenguaje "class"  seguido del nombre que se desea
class vehiculo ():
    def __init__(self): #Esta función permite asignar los parametros iniciales que tiene una clase.
        # los valores se puedne asignar ya sea por parametros o mediante funciones más adelante
        self.__km = 0 # Se define un atributo con un valor predeterminado
        # al colocar __ antes del nombre, se establece este parametro como privado (no se puede acceder fuera del objeto)
        self.__dueño = []
        self.precio =0
        self.marca =''
        self.gasolina = 10
        '''
        en este caso la función está generando los valores sobre el objeto (motivo por el cual se utiliza self
        como parametro de entrada de la función)por esto mismo no se requiere un return de la función 
        '''
    # para acceder a variables privadas se establecen funciones que permiten consultar o modificar estos valores
    def f_darkm (self):
        '''
        funcipon que retorna los km recorridos del vehiculo
        se utiliza self que es el objeto que contiene la información
        :return: retorna el km del vehiculo actual
        '''
        return self.__km
    # así mismo existen funciones que permien asignar un valor a uno de los parametros
    def f_conducir (self):
        if self.gasolina > 0:
            self.__km += 1
            self.gasolina -= 1
        else:
            print('no tiene gasolina')

    #En este caso se muestra una función que requiere de un parametro para funcionar de manera adecuada
    def f_asignar_precio (self,s_precio):
        self.precio = s_precio
        # nuevamente no se tiene un return debido a que se está generando un cambio sobre el objeto.

    def f_comprar (self, s_oferta,comprador):
        if s_oferta > self.precio:
            self.__dueño = comprador
        else:
            print ('no hay venta')

# se pueden tener multiples clases en un mismo script (aunque no es muy recomendado)
class persona ():
    # En este caso se requieren parametros para crear a una persona
    def __init__(self,nombre,cedula):
        self.nombre = nombre
        self.__cedula = cedula
'''
ahora bien, la clase por si sola no realiza ninguna función, para esto es necesario hacer el llamado de la clase 
y crear el objeto 
'''
## creación de objetos
# se crean objetos de la clase persona
p_01 = persona('pepito',12345)
p_02 = persona('pepito',12346)
print(p_01.nombre)
# print(p_01.__cedula) # como es un atributo privado no se puede acceder desde fura del objeto.

# se crean objetos de la clase vehiculo
v_01 = vehiculo() # como no se tienen parametros en la función init se puede crear sin parametros
v_01.precio = 1000 # como el atributo es publico se puede modificar sin hacer uso de funciones especiales
v_01.marca = 'x1'

print(v_01.f_darkm()) # cono km es un atributo privado se requiere la función para consultar el valor
# esta es una función que permite modificar los datos
v_01.f_conducir()
print(v_01.f_darkm())
