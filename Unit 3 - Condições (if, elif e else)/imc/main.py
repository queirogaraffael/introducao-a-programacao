peso = float(input())
altura = float(input())

imc = peso/(altura**2)

print(f"IMC = {imc:.1f}")

if imc < 18.5:
  print("Classificação = Magreza")
elif 18.5<= imc<25:
  print("Classificação = Saudável")
elif 25<=imc<30:
  print("Classificação = Sobrepeso")
else:
  print("Classificação = Obesidade")
