graus = int(input())
minutos = int(input())
segundos = int(input())

decimais = graus + minutos/60 + segundos/3600

print(f"graus = {decimais:.4f}")
