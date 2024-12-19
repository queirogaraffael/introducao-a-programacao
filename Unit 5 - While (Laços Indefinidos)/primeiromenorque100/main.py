import sys
import os

filename = "dados.dat"
if not os.path.exists(filename):
    print("O arquivo de dados (dados.dat) não existe")
    print("Execute: python3 gendata.py pra gerar o arquivo")
    sys.exit(1)

arq = open(filename)
i = 1

while True:
    linha = arq.readline()
    if linha == '': break
    num = int(linha)
    if num < 100: break
    i += 1

print(f"{num}, na posição {i}")
arq.close()