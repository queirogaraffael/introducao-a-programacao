N = int(input())

soma = 0

for i in range(N):
    numero = int(input())
    if numero % 5 == 0:
        soma += numero

print(soma)
