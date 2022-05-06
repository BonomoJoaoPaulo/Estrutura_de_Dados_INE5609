""" Sem utilizar estruturas de repetição (como for e while) ou a função len (e seus equivalentes).
Faça uma função que recebe uma string e conta o seu número de caracteres um a um,
a função deve retornar o número de caracteres total.
"""


def conta_char(string_teste):
    if string_teste == "":
        return 0
    else:
        return 1 + conta_char(string_teste[1:])


print(conta_char('paralelepipedo'))
