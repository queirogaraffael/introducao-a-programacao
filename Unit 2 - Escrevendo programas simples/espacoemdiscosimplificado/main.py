nome_1 = input()
byte_1 = int(input())
nome_2 = input()
byte_2 = int(input())
nome_3 = input()
byte_3 = int(input())

print("SPLab - Espaço utilizado pelos usuários")
print("---------------------------------------------")
print("Nr., Usuário, Espaço Utilizado")

mB_1 = (byte_1/1024)/1024
mB_2 = (byte_2/1024)/1024
mB_3 = (byte_3/1024)/1024
print("")
print(f"1, {nome_1}, {mB_1:.2f} MB")
print(f"2, {nome_2}, {mB_2:.2f} MB")
print(f"3, {nome_3}, {mB_3:.2f} MB")

total = mB_1 + mB_2 + mB_3
medio = total/3
print("")
print(f"Espaço total ocupado: {total:.2f} MB")
print(f"Espaço médio ocupado: {medio:.2f} MB")