import math

tipo = input()
hectares = float(input())

if tipo == 'Fungicida':
    unidade = math.ceil(hectares * 1.0 / 50)
    valor = unidade * 320
elif tipo == 'Herbicida':
    unidade = math.ceil(hectares * 0.3 / 1)
    valor = unidade * 100
else:
    unidade = math.ceil(hectares * 2.5 / 30)
    valor = unidade * 400

print(f"{unidade} {tipo}(s)")
print(f"R$ {valor:.2f}")
