def eh_palindromo(string_entrada):
    if string_entrada == "":
        return "Eh palindromo!"
    elif string_entrada[0] != string_entrada[-1]:
        return "NAO eh palindromo!"

    return eh_palindromo(string_entrada[1:-1])


print(eh_palindromo("rever"))

print(eh_palindromo("joao"))
