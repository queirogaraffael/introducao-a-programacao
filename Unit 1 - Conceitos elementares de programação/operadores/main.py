numero1 = int(input())
numero2 = int(input())

print("===== Operadores =====")

adicao = numero1 + numero2
subtracao = numero1 - numero2
multipilicacao = numero1*numero2
divisao = numero1/numero2
resto = numero1%numero2
exponenciacao = numero1**numero2
opostoA = -1*numero1

print(f"A = {numero1}")
print(f"B = {numero2}")

print(f"Adição = {adicao:}")
print(f"Subtração = {subtracao}")
print(f"Multiplicação = {multipilicacao}")
print(f"Divisão = {divisao}")
print(f"Resto = {resto}")
print(f"Exponenciação = {exponenciacao}")
print(f"Oposto de A = {opostoA}")

print1 = numero1 == numero2
print2 = numero1 != numero2
print3 = numero1 > numero2
print4 = numero1 < numero2
print5 = numero1 <= numero2

print(f"A é igual a B? {print1}")
print(f"A é diferente de B? {print2}")
print(f"A é maior que B? {print3}")
print(f"A é menor que B? {print4}")
print(f"A é menor ou igual a B? {print5}")