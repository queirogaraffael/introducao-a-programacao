numeros = []
soma = 0

while True:
    num = input()
    if num == "fim": break
    numeros.append(int(num))
    soma += int(num)

media = soma / len(numeros)

print(f"{media:.2f}")

for i in range(len(numeros)):
    if numeros[i] < media:
        posicao = i + 1
        print(f"{posicao} {numeros[i]}")
"""

10
6
29
3
fim
12.00
1 10
2 6
4 3"""
