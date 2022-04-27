""" Sem utilizar estruturas de repetição (while e for ), faça uma função que recebe um número n fornecido
pelo usuário e retorna uma string com os caracteres c0, c1, . . . , cn, de acordo com o seguinte padrão:
                                    CnCn−1 . . . C1C0C0C1 . . . Cn
Onde ci = i, i = 0, . . . , n
Exemplo de entrada: 4
Exemplo de saída: 4321001234
"""

string_final = ""
volta = False
count = 0


def sequencia_numeros(n):
    global string_final
    global volta
    global count
    if type(n) != int or n < 0:
        print("Por favor, tente com um valor inteiro positivo!")
        return
    else:
        if count > 1 and (string_final[0] == string_final[-1]):
            print(string_final)
            return
        if n == 0:
            volta = True
        string_final += f"{n}"
        count += 1
        if not volta:
            sequencia_numeros(n-1)
        else:
            sequencia_numeros(n+1)


sequencia_numeros(-1)
