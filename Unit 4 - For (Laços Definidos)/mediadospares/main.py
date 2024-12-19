quantidade = int(input())

soma = 0
quantidade_par = 0
todos = []

for i in range(quantidade):
  numero = int(input())
  todos.append(numero)
  if numero%2==0:
    soma += numero
    quantidade_par+=1

media = soma/quantidade_par
abaixo = 0

for i in range(quantidade):
  if media>todos[i]:
    abaixo+=1

print(f"soma: {soma}")
print(f"média: {media:.1f}")
print(f"{abaixo} número(s) abaixo da média")
