""" Implemente uma função recursiva que retorna o maior elemento de uma lista (ou array).
"""

import math


def busca_maior(array, maior_valor):
    if array[0] >= maior_valor:
        maior_valor = array[0]
    del(array[0])
    if not array:
        return maior_valor

    return busca_maior(array, maior_valor)


lista_teste = [0, 1, 3, 17, 10, 5, 4, 10]

print(busca_maior(lista_teste, -math.inf))
