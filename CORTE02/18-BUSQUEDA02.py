## 18 - BUSQUEDA BINARIA
'''
A diferencia de la busqueda secuencial en la busqueda binaria se parte de un set ordenado de datos y se van
descartando en cada iteración.
este metodo usa la recursión para obtener una aplicación eficiente de las busquedas de elementos en listas
'''

# Algoritmo

def f_busquedaBinaria(l_lista,s_target):
    s_idx = len(l_lista)//2
    s_centro = l_lista[s_idx]
    if s_centro == s_target:
        return s_centro
    elif s_centro > s_target:
        l_newList = l_lista[:s_idx]
        return f_busquedaBinaria(l_newList,s_target)
    else:
        l_newList = l_lista[s_idx:]
        return f_busquedaBinaria(l_newList, s_target)

l_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(f_busquedaBinaria(l_list,0))

#TODO: modificar el código para que retorne [] cuando no se encuentra el valor en el vector
#TODO: comparar el tiempo de ejecución de los dós metodos de busqueda para listas de distintas longitudes
#TODO: realizer un nuevo método que permita realizar la busqueda sobre letras en una cadena de caracteres.