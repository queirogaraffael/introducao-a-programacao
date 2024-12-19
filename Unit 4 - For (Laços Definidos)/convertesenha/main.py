senha = list(input())

nova_senha = []
nova_senha.append(senha[0])
troca = 0

for i in range(1,len(senha)):
    if (senha[i] == "a" or senha[i] == "A"):
        nova_senha.append("4")
        troca+=1
    elif (senha[i] == "e" or senha[i] == "E"):
       nova_senha.append("3")
       troca+=1
    elif (senha[i] == "i" or senha[i] == "I"):
       nova_senha.append("1")
       troca+=1
    elif (senha[i] == "o" or senha[i] == "O"):
       nova_senha.append("0")
       troca+=1
    else:
      nova_senha.append(senha[i])

nome = "".join(nova_senha)

print(f"{nome} ({troca} troca(s))")

