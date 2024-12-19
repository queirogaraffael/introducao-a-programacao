maior = int(input())
posicao = 1

n = 2

while n<=100:
    numero = int(input())
    if numero>maior:
        maior=numero
        posicao=n
    n+=1
    
print(f"{maior}")
print(f"{posicao}")
