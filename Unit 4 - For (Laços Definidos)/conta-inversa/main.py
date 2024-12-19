nome = input()
nome_inverso = []
controle = 0

for i in range(len(nome)):
  nome_inverso.append(nome[-i-1])
  if nome[i] == nome_inverso[i]:
    controle+=1
  
print(f"A palavra {nome} contém {controle} caractere(s) coincidente(s) com a sua inversa.")