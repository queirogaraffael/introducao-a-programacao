nomes, valores = [], []

soma = 0

nome = input()

while True:
    if nome == "**": break
    valor = input()
    if valor == "**": break
    if valor == "*":
        nomes.append(nome)
        valores.append(soma)
        soma = 0
        nome = input()
    else:
        soma += int(valor)

print("Relatório de novas questões:\n")

for i in range(len(nomes)):
    soma += valores[i]
    print(f"{nomes[i]}: {valores[i]}")

print("---")
print(f"Total de novas questões: {soma}")
"""
Jorge
2
4
8
1
10
*
Klaudio
*
João
3
1
2
*
Dalton
1
1
1
1
5
6
*
**
Relatório de novas questões:

Jorge: 25
Klaudio: 0
João: 6
Dalton: 15
---
Total de novas questões: 46"""
