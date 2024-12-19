import math 
velocidade_vazao = float(input())
diametro = float(input())
tempo = float(input())


secao = math.pi * (diametro / 2) ** 2
vazao = velocidade_vazao * secao * 1000
quant_agua = tempo * vazao

print(f"Quantidade de água = {quant_agua:.2f} litros.")