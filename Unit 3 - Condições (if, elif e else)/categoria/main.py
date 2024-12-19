nome = input()
idade = int(input())

if idade > 17:
  print(f"{nome}, {idade} anos, Senior")
elif idade >= 14:
  print(f"{nome}, {idade} anos, Juvenil B")
elif idade >= 11:
  print(f"{nome}, {idade} anos, Juvenil A")
elif idade >= 8:
  print(f"{nome}, {idade} anos, Infantil B")
elif idade >= 5:
  print(f"{nome}, {idade} anos, Infantil A")
else:
  print(f"{nome}, {idade} anos, Não pode competir.")