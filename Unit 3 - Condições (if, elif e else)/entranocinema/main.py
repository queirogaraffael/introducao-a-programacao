ano_atual = int(input("Ano atual? "))
ano_nascimento = int(input("Ano de nascimento? "))

idade = ano_atual - ano_nascimento

print(f"Idade calculada: {idade} anos")

if idade>=16:
  print("Entrada permitida")
elif idade>=14:
  acompanhado = input("Com os pais? ")
  if acompanhado == "n":
    print("Entrada proibida para menores de 16 anos sem os pais")
  else:
    print("Entrada permitida")
else:
  print("Entrada proibida para menores de 14 anos")
