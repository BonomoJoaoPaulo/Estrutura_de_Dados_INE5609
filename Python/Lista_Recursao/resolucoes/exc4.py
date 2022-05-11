import math


def sequencia_crescente(sequencia, i=0, anterior=-math.inf):
    if i == len(sequencia):
        return "True"

    elif sequencia[i] < anterior:
        return "False"

    return sequencia_crescente(sequencia, i+1, sequencia[i])


lista_exemplo = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_exemplo2 = [1, 2, 3, 10, 4, 2]

print(sequencia_crescente(lista_exemplo))
print(sequencia_crescente(lista_exemplo2))
