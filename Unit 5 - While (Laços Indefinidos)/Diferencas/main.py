modulos = []
soma = 0

while True:
    numero = input().split()
    numero1 = int(numero[0])
    numero2 = int(numero[1])
    if numero1 == 0 and numero2 == 0: break
    diferenca = abs(numero1 - numero2)
    modulos.append(diferenca)
    soma += diferenca

media = soma / len(modulos)

for i in range(len(modulos)):
    if modulos[i] > media:
        print(i + 1)
