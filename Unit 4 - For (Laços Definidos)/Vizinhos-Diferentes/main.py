# Questão Vizinhos Diferentes
#Raffael Queiroga
#Prog1 
#Prova 2
#O programa recebe N valores e armazena numa lista, e depois analisa de tras para frente se há valores adjacentes iguais, se houver, acrescenta +1 no valor da frente em relação ao ultimo número.

N = int(input())

valores = []

for i in range(N):
    numero = int(input())
    valores.append(numero)

for i in range(-1, -len(valores), -1):
    if valores[i] == valores[i - 1]:
        valores[i - 1] = valores[i] + 1

for i in range(len(valores)):
    if i == len(valores) - 1:
        print(valores[i])
    else:
        print(valores[i], end=" ")
"""

7

4
2
2
4
5
0
0
4 3 2 4 5 1 0

5

7
2
2
1
5
7 3 2 1 5"""
