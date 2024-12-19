nome1 = input()
nome2 = input()

if len(nome1)>len(nome2):
  tamanho = len(nome2)
elif len(nome2)>len(nome1):
  tamanho = len(nome1)
else:
  tamanho = len(nome1)

coincidentes = 0

print("Letras coincidentes")

for i in range(tamanho):
  if nome1[i] == nome2[i]:
    coincidentes+=1
    print(f"'{nome1[i]}' na posição {i+1}") 

porcentagem = (coincidentes/(len(nome1)+len(nome2)))*100

print(f"Total de letras coincidentes: {coincidentes} ({porcentagem:.0f}%)")