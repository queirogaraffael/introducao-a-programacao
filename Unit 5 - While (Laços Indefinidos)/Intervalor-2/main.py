N = int(input())

dentro, fora = 0,0

while N>=1:
    numero = int(input())
    if 10<=numero<=20:
        dentro+=1
    else:
        fora+=1
    N-=1

print(f"{dentro} in")
print(f"{fora} out")