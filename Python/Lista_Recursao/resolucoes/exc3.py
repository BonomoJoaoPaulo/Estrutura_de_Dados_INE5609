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
