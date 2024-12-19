K = int(input())
N = int(input())

divisiveis = 0

for i in range(N):
  numero = int(input())
  if numero%K==0:
    divisiveis+=1

porcentagem = (divisiveis/N) * 100

print(f"{divisiveis} ({porcentagem:.1f}%)")

"""9
3
20
18
15
1 (33.3%)"""