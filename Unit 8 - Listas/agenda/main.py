agenda = {}


while True:
  apoio = {}

  chave = input()
  if chave == "fim":break
  nome = input("Nome: ")
  idade = input("Idade: ")
  telefone = input("Telefone: ")
  apoio = {"nome": nome, "idade": idade, "telefone": telefone}
  agenda[chave] = apoio


for chave in agenda:
  print(agenda[chave])



"""
2. Crie um dicionário que é uma agenda e
coloque nele os seguintes dados: chave (cpf),
nome, idade, telefone. O programa deve ler
um número indeterminado de dados, criar a
agenda e imprimir todos os itens do
dicionário no formato chave: nome-idade-
fone.
"""
