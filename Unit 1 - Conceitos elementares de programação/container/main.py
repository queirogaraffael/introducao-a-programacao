capacidade = int(input())
capacidade_p = int(input())

final1 = capacidade//120
final2 = capacidade - final1*120 

final3 = final2//capacidade_p

final4 = final2 - final3*capacidade_p

print(f"O container comporta {final1:.0f} caixa(s) grande(s).")
print(f"O container comporta {final3:.0f} caixa(s) pequena(s).")
print(f"Há {final4:.0f}kg de capacidade restante.")