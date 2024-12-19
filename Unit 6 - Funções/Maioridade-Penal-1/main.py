#Questão Maioridade Penal
#Raffael Queiroga
#Prog1
#Prova 2
#O programa analisa quem tem igual ou maior que 18 anos e imprime na tela, a fim de mostrar quem jáá se enquadra na maioridade penal.

nomes = input().split()
idades = input().split()

for i in range(len(idades)):
    if int(idades[i]) >= 18:
        print(nomes[i])
"""
Jansen Italo Ana
14 21 60
Italo
Ana"""
