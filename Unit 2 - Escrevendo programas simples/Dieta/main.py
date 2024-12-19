kg = float(input())
tempo = float(input())
calorias_consumida = float(input())

dias = (kg * 7700) / (2000+900*tempo-calorias_consumida)

print(f"Você precisará de {dias:.2f} dias de dieta")