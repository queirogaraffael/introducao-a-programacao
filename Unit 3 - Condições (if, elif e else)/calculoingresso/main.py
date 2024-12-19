idade = int(input("Idade: "))

nome = "anônimo"
documento = ""

if idade<=18:
  if 12<=idade<=18:
    nome = input("Nome: ")
    documento = input("Documento: ")
  preco = "10.00"
elif 18<idade<60:
    preco = "20.00"
else:
  nome = input("Nome: ")
  documento = input("Documento: ")
  preco = "12.00"

print("===")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Documento: {documento}")
print(f"Preço: {preco}")

