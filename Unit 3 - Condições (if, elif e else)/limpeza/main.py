servico = int(input())

if servico ==1:
    tamanho = int(input())
    total = tamanho * 80.00
    if total>=200:
      print(f"R$ {total:.0f},00")
      print("Brinde!")
    else:
      print(f"R$ {total:.0f},00")
elif servico==2:
    tamanho = int(input())
    total = tamanho * 50.00
    if total>=200:
      print(f"R$ {total:.0f},00")
      print("Brinde!")
    else:
      print(f"R$ {total:.0f},00")
else:
  print("R$ 50,00")
