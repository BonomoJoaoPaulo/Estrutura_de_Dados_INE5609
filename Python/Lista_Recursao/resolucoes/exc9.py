""" Implemente uma função recursiva que recebe n e retorna o valor da soma
1**1 + 2**2 + 3**3 + . . . + n**n.
"""


def soma_potencias(n, soma=0):
    soma += n**n
    if n == 1:
        print(soma)
        return
    soma_potencias(n-1, soma)


soma_potencias(4)
