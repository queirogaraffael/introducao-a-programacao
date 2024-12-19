valor = float(input('Valor (R$): '))
tipo = input('(D)ébito ou (C)rédito: ')

if tipo == 'd' or tipo == 'D':
  valor_liquido = valor * 0.97
  print(f"Valor líquido a receber: {valor_liquido:.2f}")
elif tipo == 'c' or tipo == 'C':
  valor_liquido = valor * 0.95
  print(f"Valor líquido a receber: {valor_liquido:.2f}")
else:
  print('Tipo incorreto. Tente novamente.')