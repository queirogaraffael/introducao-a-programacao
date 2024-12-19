cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())


cpf11 = cpf1//100 # ta certo
digitos1 = cpf1%100
soma_digitos1 = (digitos1//10) + (digitos1%10)

cpf22 = cpf2//100
digitos2 = cpf2%100
soma_digitos2 = (digitos2//10) + (digitos2%10)

cpf33 = cpf3//100
digitos3 = cpf3%100
soma_digitos3 = (digitos3//10) + (digitos3%10)


print(f"{cpf11}-{digitos1}")
print(soma_digitos1)

print(f"{cpf22}-{digitos2}")
print(soma_digitos2)

print(f"{cpf33}-{digitos3}")
print(soma_digitos3)
