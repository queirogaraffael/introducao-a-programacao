valor_total = float(input())
data = input()
quantidade_de_produtos = int(input())

media = valor_total / quantidade_de_produtos
print (f'Data: {data}')
print (f'O valor total da compra foi de R$ {valor_total:.2f}. A média do preço dos produtos é de {media:.1f}.')