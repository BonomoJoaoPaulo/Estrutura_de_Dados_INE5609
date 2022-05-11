def printa_ultimo_char(string_teste):
    if string_teste == "":
        return
    print(string_teste[-1])

    return printa_ultimo_char(string_teste[:-1])


printa_ultimo_char('paralelepipedo')
