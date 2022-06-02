def conta_char(string_teste):
    if string_teste == "":
        return 0
    else:
        return 1 + conta_char(string_teste[1:])


print(conta_char('paralelepipedo'))
