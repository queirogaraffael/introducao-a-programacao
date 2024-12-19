inicial = int(input())
final = int(input())

repeticao = final - inicial + 1

abaixo, acima = 0, 0
soma1, soma2 = 0, 0

for i in range(repeticao):
    salario = float(input())

    if salario <= 100:
        soma1 += salario
        abaixo += 1
    else:
        soma2 += salario
        acima += 1

if abaixo == 0 and acima > 0:
    porcentagem2 = (acima / repeticao) * 100
    media_acima = soma2 / acima
    porcentagem1,media_abaixo = 0,0
    media_abaixo = 0
elif acima == 0 and abaixo > 0:
    porcentagem1 = (abaixo / repeticao) * 100
    media_abaixo = soma1 / abaixo
    porcentagem2, media_acima = 0, 0
else:
    porcentagem1 = (abaixo / repeticao) * 100
    media_abaixo = soma1 / abaixo
    porcentagem2 = (acima / repeticao) * 100
    media_acima = soma2 / acima

print(f"{abaixo} ano(s) abaixo ({porcentagem1:.0f}% dos anos)")
if media_abaixo>0:
  print(f"média dos anos abaixo: U$ {media_abaixo:.2f}")

print(f"{acima} ano(s) acima ({porcentagem2:.0f}% dos anos)")
if media_acima>0:
  print(f"média dos anos acima: U$ {media_acima:.2f}")

