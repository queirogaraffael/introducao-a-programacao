kg_antes = float(input())
kg_depois = float(input())

porcentagem = (100- (kg_depois*100)/kg_antes)

if porcentagem >= 10:
  print(f"{porcentagem:.1f}% do peso do produto é de água congelada.")
  print("Produto não conforme")
elif porcentagem >= 5:
   print(f"{porcentagem:.1f}% do peso do produto é de água congelada.")
   print("Produto em conformidade")
else:
  print(f"{porcentagem:.1f}% do peso do produto é de água congelada.")
  print("Produto Qualis A.")