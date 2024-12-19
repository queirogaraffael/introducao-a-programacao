binarios = []

while True:
    numero = input()
    if numero == "fim": break
    binarios.append(numero)

for i in range(len(binarios)):
    numero = binarios[i]
    numero1 = numero[:4]
    numero2 = numero[4:]

    if len(numero) != 8:
        print("Tente novamente.")
    elif int(numero1, 2) > 9 or int(numero2, 2) > 9:
        print("BCD inválido.")
    else:
        numero_final1 = int(numero1, 2)
        numero_final2 = int(numero2, 2)
        print(f"{numero_final1}{numero_final2}")
        
"""
python joao.py
11110101
fim
BCD inválido.

python joao.py
1111
fim
Tente novamente.

python joao.py
10101010
10001000
fim
BCD inválido.
88  """
