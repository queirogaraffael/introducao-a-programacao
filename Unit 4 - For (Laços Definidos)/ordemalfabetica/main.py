N = int(input())

palavras = []

antes, depois = 0, 0

for i in range(N):
    palavras.append(input())

print("---")

palavra_referencia = input()

for i in palavras:
    if i != palavra_referencia:
        if i > palavra_referencia:
            depois += 1
        else:
            antes += 1

print(f"{antes} antes")
print(f"{depois} depois")



