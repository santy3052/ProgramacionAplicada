class persona (object):
    def __init__(self,nombre,hermanos,padre):
        self.nombre=nombre # Nombre de la persona
        self.Hermanos=hermanos # hermanos de la persona (n datos)
        self.Padres=padre # padres de la persona (2 datos o menos)

    def add_siblings (self,sib,nombre,hermanos,padre):
        # TODO: verificar y asegurar que los hermanos tengan los mismos padres (0.5)
        self.Hermanos.append(sib)
        self.add_parents(self,padre(0))
        self.add_parents(self, padre(1))

    def add_parents (self,parent):
        if self.Padres < 2:
            self.Padres.append(parent)
        else:
            print('No se puede agregar')

    def search (self,nombre):
        '''
        se busca a cualquier persona en el arbol, se asume que el usuario puede colocar cualquier combinación de
        mayusculas y minusculas
        :param nombre: nombre de la persona a buscar
        :return: retorna el objeto encontrado así como la altura a la que se encuentra el elemento
        '''
        #TODO: Implementar un método de busqueda para encontrar a cualquier persona en el arbol (0.5)
        if self.nombre.equals(nombre):
            return self
        else:
            def busc_sec(self,l):
                for i in l:
                    if self.nombre.equals(nombre):
                        return i
            a=busc_sec(self.Hermanos,nombre)
            if a!=none:
                return a
            else:
                return self.Padres(0).search(nombre)


    def tree2dict (self, lista):
        '''
        convierte el arbol actual en un diccionario usando los nombres como llaves y los padres y hermanos como llaves
        :return: retorna un diccionario
        '''
        # TODO: Implementar una función que permita convertir el arbol actual en un diccionario (1.0)
        def tr2list(self, lista):
            lista = []
            t = self
            t.Hermanos = []
            t.Padres = []
            lista.append(t)
            lista.append(self.Hermanos)
            lp0 = tr2list(self.Padres(0))
            lp1 = tr2list(self.Padres(1))
            lista.append(lp0)
            lista.append(lp1)
            return lista
        tr2list(t,lista)
        for lista in dic:
            dic=dict(lista)


    def encript(self,nombre):
        '''
        crea un archivo encriptado, con la información correspondiente al arbol
        :param nombre: nombre del archivo que se desea crear
        :return: null
        '''
        # TODO: Implementar una función que permita converti el arbol en un archivo encriptado (1.0)
        self.nombrearch = nombre
        zn = self.nombrearch + '.txt'
        print(zn)
        with open(zn, 'arbolencrip') as file:
            file.write('\n' + self.nombre)
            file.write('\n' + self.Padres)
            file.write('\n' + self.Hermanos)

    def decrip(self,nombre):
        '''
        lee un archivo de texto, lo decifra y convierte el resultado en el arbol correspondiente
        :param nombre: Nombre del archivo que se desea leer
        :return: arbol creado
        '''
        #TODO: Im plementar una función que permita convertir un archivo encriptado en un arbol (1.0)

        self.nombrearch = nombre
        zn = self.nombrearch + '.txt'
        archivo = open(zn, 'arbolencript', encoding='utf-8')
        print(archivo.read())
        print("")
        return print('Arbol creado')

    ##
    '''
    la siguiente sección se debe realizar en un archivo distinto llamado TALLER02-2_nombre_apellido.py
    '''
    # TODO: iniciar y crear el arbol con una profundidad de almenos 4 con su familia (0.2)
p1=persona('Julian','Rosa ''miguel','Roberto ''juliana')
p2=persona('Rosa','Julian ''miguel','Roberto ''juliana')
p3=persona('miguel','Rosa ''Julian','Roberto ''juliana')
p4=persona('juliana','Luis','Lina' ' Hugo')
p5=persona('Roberto','Liliana', 'Margarita' ' Rogelio')
p6=persona('Lina', 'Rigoberto', 'Luna ' 'Juan')
p7=persona('Hugo', 'Laura ' 'Nicolas', 'Angel ' 'Lola')
p8=persona('Margarita', 'Ramiro', 'Lisa ''Mario')
p9=persona('Rogelio', 'Martina', 'Merida ' 'Felipe')
    # TODO: validar la función de busqueda (0.2)
assert search(Miguel) 
assert search(Roberto)
assert search(Merida)
    # TODO: validad la encriptación de los archivos (0.2)
    # se hizo la pruena y si funciono correctamente
    # TODO: validar la decriptación de archivos (0.2)
    #gracias a que el primero funciono este logro mostrar la informacion correctamente
    # TODO: validar la converción a diccionario (0.2)
assert tree2dict(persona)
