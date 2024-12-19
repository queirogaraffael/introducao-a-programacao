def print_media(media, penalizacao):
    if media>6.0:
        print(f"Média: {media:.1f} (aprovado)")
    else:
      print(f"Média: {media:.1f} (cursando)")

    print(f"Penalização: {penalizacao:.1f}\n")


print(f"Mastery Learning")
print(f"Cálculo da nota na unidade\n")

penalizacao = -0.5

nota1 = float(input("Nota? "))
nota2 = float(input("Nota? "))

while True:
    media = (nota1 + nota2) / 2
    penalizacao += 0.5
    if media >= 6.0:
        print_media(media, penalizacao)
        break
    else:
        print_media(media, penalizacao)

    nota = float(input("Nota? "))

    if nota > nota1:
        nota1 = nota
    elif nota > nota2:
        nota2 = nota
    else:
        continue

media_final = media - penalizacao

print("===")
print(f"Notas válidas: {nota1:.1f} e {nota2:.1f}")
print(f"Média parcial na unidade: {media:.1f}")
print(f"Penalizações: {penalizacao:.1f}")
print(f"Média final na unidade: {media_final:.1f}")
"""
Nota? 4.0
Nota? 6.0
Média: 5.0 (cursando)
Penalização: 0.0

Nota? 3.0
Média: 5.0 (cursando)
Penalização: 0.5

Nota? 7.0
Média: 6.5 (aprovado)
Penalização: 1.0

===
Notas válidas: 7.0 e 6.0
Média parcial na unidade: 6.5
Penalizações: 1.0
Média final na unidade: 5.5"""
