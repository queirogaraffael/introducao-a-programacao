def dentro(numero, lista):
    for i in range(len(lista)):
        if numero == lista[i]:
            return True
    return False


def indice(valor, lista):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i


nomes, cpfs, preferidos, saldos = [], [], [], []

nome_cadastro, cpf_cadastro, preferido_cadastro = [], [], []
cpf_atualizar, preferido_atualizar = [], []
consultas = []

while True:
    opcao = input()
    if opcao == "finalizar": break
    if opcao == "cadastrar":
        cpf_cadastro.append(input())
        nome_cadastro.append(input())
        preferido_cadastro.append(input())
    elif opcao == "atualizar":
        cpf_atualizar.append(input())
        preferido_atualizar.append(input())
    else:
        consultas.append(input())

for i in range(len(nome_cadastro)):
    if not dentro(cpf_cadastro[i], cpfs):
        saldos.append(300)
        nomes.append(nome_cadastro[i])
        cpfs.append(cpf_cadastro[i])
        preferidos.append(preferido_cadastro[i])
        print("Usuário cadastrado com sucesso.")
    else:
        print("Usuário já existente.")

for i in range(len(cpf_atualizar)):
    if not dentro(cpf_atualizar[i], cpfs):
        print("Usuário inexistente.")
    else:
        print("Usuário atualizado com sucesso.")
        ind = indice(cpf_atualizar[i], cpfs)
        if preferido_atualizar[i] == preferidos[ind]:
            saldos[ind] += 200
        else:
            saldos[ind] += 100

for i in range(len(consultas)):
    if not dentro(consultas[i], cpfs):
        print("Usuário inexistente.")
    else:
        ind = indice(consultas[i], cpfs)
        print(f"Nome: {nomes[ind]}")
        print(f"CPF: {consultas[i]}")
        print(f"Saldo: {saldos[i]:.2f}")
"""
cadastrar
022.222.333-99
Antoine
Posto 15
cadastrar
011.233.567.78
Josephine
Posto 1
finalizar
Usuário cadastrado com sucesso.
Usuário cadastrado com sucesso.


$ python meu_posto.py
cadastrar
022.222.333-99
Antoine
Posto 15
consultar
022.222.333-99
finalizar
Usuário cadastrado com sucesso.
Nome: Antoine
CPF: 022.222.333-99
Saldo: 300.00


$ python meu_posto.py    
atualizar
022.222.333-80
Posto 15
finalizar
Usuário inexistente.
"""

cadastrar
raffael
700.639.333-26
posto 15
cadastrar
raffael
700.639.333-26
posto 15

atualizar
700.639.333-26
posto 15
atualizar
700.639.333-26
posto 16
atualizar
700.633.333-28
posto 19