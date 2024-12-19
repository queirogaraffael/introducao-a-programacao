comprimento = float(input())
largura = float(input())

comprimento_m = comprimento * 0.01 * 2
largura_m = largura * 0.01 * 2 

total = (comprimento_m+largura_m) * 120

print(f"R$ {total:.1f}")