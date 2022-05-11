""" Sem utilizar estruturas de repetição (while e for ), faça uma função que recebe um número n fornecido
pelo usuário e retorna uma string com os caracteres c0, c1, . . . , cn, de acordo com o seguinte padrão:
                                    CnCn−1 . . . C1C0C0C1 . . . Cn
Onde ci = i, i = 0, . . . , n
Exemplo de entrada: 4
Exemplo de saída: 4321001234
"""


def sequencia_numeros(n, count=0, n_inicial=0, volta=False, string_final=""):
    if type(n) != int or n < 0:
        return "Por favor, tente com um valor inteiro positivo!"
    else:
        if count == 0:
            n_inicial = n
        if n == 0:
            volta = True

        string_final += f"{n} "
        count += 1
        if volta:
            if count > 1 and n == n_inicial:
                return string_final

            return sequencia_numeros(n+1, count, n_inicial, volta, string_final)

    return sequencia_numeros(n-1, count, n_inicial, volta, string_final)


print(sequencia_numeros(10))
