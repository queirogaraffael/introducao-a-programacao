numero = input()

base = 2**(len(numero)-1)

soma= 0

for i in range(len(numero)):
  resultado = int(numero[i]) * base
  print(f"{numero[i]} * {base:.0f} = {resultado:.0f}")
  soma+=resultado
  base/=2


print(f"{numero}(2) = {soma:.0f}(10)")