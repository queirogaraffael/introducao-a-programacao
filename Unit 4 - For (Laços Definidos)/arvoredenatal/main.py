n = int(input())

tronco = "o"

print(f"{tronco: >{n}s}")

for i in range(1,n):
  print(f"{i*tronco: >{n-1}s}{tronco}{i*tronco}")

print(f"{tronco: >{n}s}")