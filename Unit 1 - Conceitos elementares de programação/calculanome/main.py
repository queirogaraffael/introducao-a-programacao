nome = input("Nome? ")
valor = float(input("Valor da letra (R$)? "))

tamanho = len(nome)
preco = tamanho * valor

print(f"Preço final: R$ {preco:.2f}")