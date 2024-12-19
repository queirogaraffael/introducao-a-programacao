nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
peso1 = float(input())
peso2 = float(input())

peso3 = 1 - (peso1/100) - (peso2/100)

media = ((nota1*peso1/100)+ (nota2*peso2/100) + (nota3*peso3)/((peso1/100) + (peso2/100) +peso3))

print(f"Média Final: {media:.1f}")