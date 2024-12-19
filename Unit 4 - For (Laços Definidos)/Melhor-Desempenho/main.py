N = int(input())
res = []
maior = 0

for i in range(N):
    contador = 0
    resultado = list(input())
    for i in range(len(resultado)):
        if resultado[i] == ".":
            contador += 1
    res.append(contador)

for i in range(len(res)):
    if res[i] > maior:
        maior = res[i]
        aluno = i + 1

    if maior == 0:
        aluno = -1

print(aluno)
"""
3
fff**FFf
...fff**
.****.ff
0


3
...**FFf
.fffff**
.****.ff
1

-1"""
