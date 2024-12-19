categorias = []

somador = 0

while True:
    codigo = input()
    if codigo == "S": break
    if codigo[0] == "R":
        categorias.append(codigo[2])
    else:
        for i in range(len(categorias)):
            if codigo[2] == categorias[i]:
                somador += 1
        print(somador)
        somador = 0
"""
registro e categorias

R A12345
R A12345
P A
2
R A00007
P A
3
R B90000
P B
1
R B90001
P B
2
S"""
