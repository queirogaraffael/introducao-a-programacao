quantidade_morango = int(input())

numero_de_caixas = quantidade_morango//400

porcentagem = (quantidade_morango - numero_de_caixas*400)*100/quantidade_morango

print(f"{numero_de_caixas} caixa(s) completa(s) para embalar os morangos.")
print(f"{porcentagem:.1f}% dos morangos serão perdidos.")