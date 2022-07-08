def soma_intervalo(n, soma=0):
    soma += n
    if n == 1:
        return soma

    return soma_intervalo(n-1, soma)


print(soma_intervalo(6))
