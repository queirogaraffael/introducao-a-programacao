idade = int(input("Idade? "))

if idade < 12:
  print("criança (meia entrada)")
elif idade>=65:
  print("idoso (meia entrada)")
else:
  estudante = input("Estudante? ")
  if estudante == "n":
    print("adulto (inteira)")
  else:
    rede_publica = input("Rede Pública? ")
    if rede_publica == "s":
      print("estudante da rede pública (isento)")
    else:
      print("estudante (meia entrada)")