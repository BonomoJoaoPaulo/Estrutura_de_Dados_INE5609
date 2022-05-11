def soma_potencias(n, soma=0):
    soma += n**n
    if n == 1:
        return soma

    return soma_potencias(n-1, soma)


print(soma_potencias(3))
