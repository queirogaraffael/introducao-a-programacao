numero = input()
soma = 0

for i in range(len(numero)):
  soma += int(numero[i])

digito = soma % 11

if digito == 10:
  print(f"{numero}-X")
else:
  print(f"{numero}-{digito}")
