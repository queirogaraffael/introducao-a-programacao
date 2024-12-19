razao = float(input())
kg_maximo = float(input())

adultos, idosos, criancas, kg, control = 0, 0, 0, 0, 0
controle = True

while True:
    entrada = input().split()
    resultado1 = entrada[0]

    if controle == True and (resultado1 == "i" or resultado1 == "c"):break

    controle = False

    if resultado1 == "a":
        adultos += 1
        control = 1
    elif resultado1 == "i":
        idosos += 1
        control = 2
    else:
        criancas += 1
        control = 3

    if ((criancas + idosos) / adultos) > razao:
        if control == 1:
            adultos -= 1
        elif control == 2:
            idosos -= 1
        else:
            criancas -= 1
        break

    kg += float(entrada[1])
    if kg > kg_maximo:
        if control == 1:
            adultos -= 1
        elif control == 2:
            idosos -= 1
        else:
            criancas -= 1
        kg -= float(entrada[1])
        break

pessoas = adultos + idosos + criancas

print(f"Ônibus saiu com {pessoas} pessoa(s) e {kg:.2f} kg.")
print(f"{adultos} adulto(s), {idosos} idoso(s) e {criancas} criança(s).")
