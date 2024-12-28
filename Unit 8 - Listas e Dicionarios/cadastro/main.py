dicionario = {}
menores = {}
chaves_remover = []

while True:
    apoio = {}
    chave = input()
    if chave == "fim": break
    nome = input()
    idade = int(input())
    apoio = {"nome": nome, "idade": idade}
    dicionario[chave] = apoio

for i in dicionario:
    if dicionario[i]["idade"] < 18:
        apoio = {}
        apoio.update(dicionario[i])
        menores[i] = apoio
        chaves_remover.append(i)

for i in range(len(chaves_remover)):
    del dicionario[chaves_remover[i]]

print(menores)
print(dicionario)
"""
3. Crie um programa que cadastre
informações de várias pessoas (nome,
idade e cpf) e depois coloque em um
dicionário. Depois remova todas as
pessoas menores de 18 anos do
dicionário e coloque em outro dicionário.
"""
