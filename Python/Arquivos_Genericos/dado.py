from random import randrange

count_um = 0
count_dois = 0
count_tres = 0
count_quatro = 0
count_cinco = 0
count_seis = 0
count_total = 0


while count_total != 100:
    i = randrange(1, 7)
    if i == 1:
        count_um += 1
    elif i == 2:
        count_dois += 1
    elif i == 3:
        count_tres += 1
    elif i == 4:
        count_quatro += 1
    elif i == 5:
        count_cinco += 1
    else:
        count_seis += 1

    count_total += 1

print(f"Vezes que o dado caiu em 1: {count_um}.\n"
      f"Vezes que o dado caiu em 2: {count_dois}.\n"
      f"Vezes que o dado caiu em 3: {count_tres}.\n"
      f"Vezes que o dado caiu em 4: {count_quatro}.\n"
      f"Vezes que o dado caiu em 5: {count_cinco}.\n"
      f"Vezes que o dado caiu em 6: {count_seis}.\n")
