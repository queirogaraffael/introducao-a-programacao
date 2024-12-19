# Questão Soma 5 abaixo de 20
#Raffael Queiroga
#Prog1
#Prova 2
#O programa lê dados atráves de um arquivo e analisa os 5 numeros menores que 20 e soma os em uma variavel e grava a posicao do ultimo numero menor 20 lido. E imprime todos esses dados.

filename = "dados.txt"

arq = open(filename)
quantidade, soma, posicao_final, i = 0, 0, 0, 1

while True:
    linha = arq.readline()
    if linha == '' or quantidade == 5: break
    num = int(linha)
    if num < 20:
        posicao_final = i
        soma += num
        quantidade += 1
    i += 1

arq.close()

print(f"soma = {soma}")
print(f"{quantidade} menores que 20 até a linha {posicao_final}")
