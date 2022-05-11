def indice_primeiro_par(array, i=0):
    if array[i] % 2 == 0:
        return i
    return indice_primeiro_par(array, i+1)


lista_teste = [1, 3, 5, 7, 6]

print(indice_primeiro_par(lista_teste))
