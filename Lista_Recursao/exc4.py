""" Sem utilizar estruturas de repetição (while e for ), faça uma função que verifica se uma sequência de
valores numéricos é estritamente crescente. Isto é, verifica se o elemento na posição i é estritamente
menor do que o elemento na posição i + 1. A função deve retornar True se a sequência é estritamente
crescente, caso contrário, deve retornar False
Exemplo de entrada: 1 2 3 10 4 2
Exemplo de saída: False
"""


import math


def sequencia_crescente(sequencia, i=0, anterior=-math.inf):
    if i == len(sequencia):
        print("True")
        return

    if sequencia[i] > anterior:
        sequencia_crescente(sequencia, i+1, sequencia[i])
    else:
        print("False")
        return


lista_exemplo = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_exemplo2 = [1, 2, 3, 4, 5, 3]

sequencia_crescente(lista_exemplo)
sequencia_crescente(lista_exemplo2)
