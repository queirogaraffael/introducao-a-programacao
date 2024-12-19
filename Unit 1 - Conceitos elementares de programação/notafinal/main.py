print("== Estágio 1 ==")
peso1 = float(input("Peso? "))
nota1 = float(input("Nota? "))

print("== Estágio 2 ==")
peso2 = float(input("Peso? "))
nota2 = float(input("Nota? "))

print("== Estágio 3 ==")
peso3 = float(input("Peso? "))
nota3 = float(input("Nota? "))

media_parcial = (nota1*peso1 + nota2*peso2 + nota3 *peso3)/(peso1+peso2+peso3)

nota_minima = (5.0 - (media_parcial * 0.6))/0.4
nota_final2 = (7.0 - (media_parcial * 0.6))/0.4

print("== Resultados ==")

print(f"Média parcial: {media_parcial:.1f}")
print(f"Nota na final, pra média 5.0 = {nota_minima:.1f}")
print(f"Nota na final, pra média 7.0 = {nota_final2:.1f}")
