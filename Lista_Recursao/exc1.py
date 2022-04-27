""" Sem utilizar estruturas de repetição (como for e while) ou a função len (e seus equivalentes).
Faça uma função que recebe uma string e conta o seu número de caracteres um a um,
a função deve retornar o número de caracteres total."""

count = 0


def conta_char(string_teste):
    global count
    if string_teste != "":
        count += 1
        conta_char(string_teste[1:])
    return count


print(conta_char('paralelepipedo'))
