soma, denominador, media = 0, 0, 0

while True:
    valor = float(input())
    if valor < media: break
    denominador += 1
    soma += valor
    media = soma / denominador


print(f"Saldo total do FIS: R${soma:.2f}.")
print(f"Média das contribuições: R${media:.2f}.")
"""
2.30
2.30
10.40
5.60
1.20

Saldo total do FIS: R$20.60.
Média das contribuições: R$5.15."""
