""" Implemente uma função recursiva que recebe uma lista de valores inteiros e retorna a posição do primeiro
valor par da lista.
"""


def indice_primeiro_par(array, i=0):
    if array[i] % 2 == 0:
        print(i)
        return
    indice_primeiro_par(array, i+1)


lista_teste = [1, 3, 5, 7, 6]

indice_primeiro_par(lista_teste)
