total = int(input())
teresa = int(input())
carla = int(input())
joaquim = total - teresa - carla

porcentagem1 = (teresa / total) * 100
porcentagem2 = (joaquim / total) * 100
porcentagem3 = (carla / total) * 100

print(f"Teresa vendeu {teresa} (de {total}) brinquedos. ({porcentagem1:.2f}%)")

print(f"Joaquim vendeu {joaquim} (de {total}) brinquedos. ({porcentagem2:.2f}%)")

print(f"Carla vendeu {carla} (de {total}) brinquedos. ({porcentagem3:.2f}%)")
