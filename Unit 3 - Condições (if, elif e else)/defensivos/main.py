import math 

tipo = input()
hectares = float(input())

unidade = 1

if tipo=='Fungicida':
  litros = 1.0 * hectares
  if litros<=50:
    total = 320
  else:
    unidade = litros/50
    total = (math.ceil(unidade)) * 320
  print(f"{math.ceil(unidade)} Fungicida(s)")
  print(f"R$ {total:.2f}")
elif tipo=='Inseticida':
  litros = 2.5 * hectares
  if litros<=30:
    total = 400
  else:
    unidade = litros/30
    total = (math.ceil(unidade)) * 400
  print(f"{math.ceil(unidade)} Inseticida(s)")
  print(f"R$ {total:.2f}")
else:
  litros = 0.3 * hectares
  unidade = math.ceil(litros)
  print(f"{math.ceil(unidade)} Herbicida(s)")
  print(f"R$ {total:.2f}")
