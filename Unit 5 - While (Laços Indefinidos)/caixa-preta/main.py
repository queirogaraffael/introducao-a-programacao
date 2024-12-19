peso1, combustivel1, altitude1 = 0, 0, 0

while True:
    dados = input().split()

    peso = int(dados[0])
    combustivel = int(dados[1])
    altitude = int(dados[2])

    nome = "dado inconsistente. peso negativo."

    if peso >= 0:
        peso1 += 1
        nome = "dado inconsistente. combustível negativo."
        if combustivel >= 0:
            combustivel1 += 1
            nome = "dado inconsistente. altitude negativa."
            if altitude >= 0:
                altitude1 += 1

    if peso < 0 or combustivel < 0 or altitude < 0: break

print(f"{nome}")
print(f"peso: {peso1}")
print(f"combustível: {combustivel1}")
print(f"altitude: {altitude1}")
"""
10 2 3
3 1 -1
dado inconsistente. altitude negativa.
peso: 2
combustível: 2
altitude: 1

python solution.py
1 2 4
-1 2 3
dado inconsistente. peso negativo.
peso: 1
combustível: 1
altitude: 1"""
