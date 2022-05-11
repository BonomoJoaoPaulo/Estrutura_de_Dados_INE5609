""" Sem utilizar estruturas de repetição (como for e while) ou a função reverse (e suas variações),
faça uma função que recebe uma string e imprime os caracteres dessa string, um por linha, em ordem invertida.
"""


def printa_ultimo_char(string_teste):
    if string_teste == "":
        return
    print(string_teste[-1])

    return printa_ultimo_char(string_teste[:-1])


printa_ultimo_char('paralelepipedo')
