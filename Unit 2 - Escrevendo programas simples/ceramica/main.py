capac_revestimento = float(input("Capacidade de revestimento?"))
print("\n")
print("== Dados do vão a revestir ==")

comprimento = float(input("Comprimento? "))
largura = float(input("Largura? "))
altura = float(input("Altura?"))

area_total = comprimento * largura + 2* comprimento * altura + 2 * altura *largura
n_caixas = area_total /capac_revestimento

print("\n")
print("== Resultados ==")

print(f"Área total a revestir: {area_total:.1f} m2")
print(f"Número de caixas: {n_caixas:.0f}")

