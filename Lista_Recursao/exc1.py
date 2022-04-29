""" Sem utilizar estruturas de repetição (como for e while) ou a função len (e seus equivalentes).
Faça uma função que recebe uma string e conta o seu número de caracteres um a um,
a função deve retornar o número de caracteres total."""


def conta_char(string_teste, count):
    if string_teste == "":
        print(count)
        return
    count += 1
    conta_char(string_teste[1:], count)


conta_char('paralelepipedo', 0)
