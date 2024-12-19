N = int(input())

soma_par = 0
soma_impar = 0
impar, par = 0, 0

for i in range(N):
    numero = int(input())
    if numero % 2 == 0:
        soma_par += numero
        par += 1
    else:
        soma_impar += numero
        impar += 1

media_par = soma_par / par
media_impar = soma_impar / impar

print(f"pares: {par}")
print(f"ímpares: {impar}")
print(f"média pares: {media_par:.1f}")
print(f"média ímpares: {media_impar:.1f}")
