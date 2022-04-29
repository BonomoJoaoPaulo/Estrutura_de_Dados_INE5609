""". Implemente uma função recursiva que recebe uma string e retorna se a string é ou não um palíndromo,
isto é, se a string é a mesma se lida da direita para a esquerda ou esquerda para a direita.
Exemplo de palíndromos: “12321”, “radar”, “xxx++xxx”.
"""


def eh_palindromo(string_entrada):
    if string_entrada == "":
        print("Eh palindromo!")
        return
    if string_entrada[0] == string_entrada[-1]:
        eh_palindromo(string_entrada[1:-1])
    else:
        print("NAO eh palindromo.")
        return


eh_palindromo("rever")

eh_palindromo("joao")
