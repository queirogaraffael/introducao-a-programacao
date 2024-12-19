nome = input()
vendas = float(input())

if vendas<= 499.99:
  comissao = vendas * 0.02
elif 500<=vendas<=999.99:
  comissao = vendas * 0.03
else:
  comissao = vendas * 0.04

print(f"O valor da comissão para o(a) vendedor(a) {nome} é R$ {comissao:.2f}.")
