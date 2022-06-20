## 17-BUSQUEDA SECUENCIAL
'''
En esta sección veremos un algoritmo de busqueda, la busqueda secuencial.

este algoritmo consiste en mirar cada uno de los datos de una lista hasta encontrar el dato que corresponde
'''

def f_busqueda_Secuencial(l_List,s_target):
    for idx in range(len(l_List)):
        s_temp = l_List[idx]
        if s_temp == s_target:
            return idx
    print('no se encotró el valor')
    return []

l_lis = [0,1,2,3,4,5,6,7,8,9]
s_target = 11
print(f_busqueda_Secuencial(l_lis,s_target))

# TODO: realizar cambios en las listas y los indices para observar el comportamiento de la funcíón
# TODO: revisar si el algoritmo funciona para cadenas de caracteres y en caso de no funcionar modificarlo