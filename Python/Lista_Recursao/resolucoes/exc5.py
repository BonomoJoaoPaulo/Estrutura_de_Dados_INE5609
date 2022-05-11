""" Implemente uma função que recebe um valor inteiro n e retorna a soma dos números inteiros no intervalo
[1, n].
"""


def soma_intervalo(n, soma=0):
    soma += n
    if n == 1:
        return soma
    else:
        return soma_intervalo(n-1, soma)


print(soma_intervalo(6))
