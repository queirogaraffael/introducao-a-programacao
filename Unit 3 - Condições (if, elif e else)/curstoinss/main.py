salario = float(input())

salario_empregador = salario * 0.12

print(f"O valor da contribuição do INSS a ser pago pelo empregador é de R$ {salario_empregador:.2f}")

if salario > 2195.12:
  salario = salario *0.11
  print(f"O valor da contribuição do INSS a ser pago pelo empregado é de R$ {salario:.2f}")
elif 1317.08<=salario<=2195.12:
  salario = salario *0.09
  print(f"O valor da contribuição do INSS a ser pago pelo empregado é de R$ {salario:.2f}")
else:
  salario = salario *0.08
  print(f"O valor da contribuição do INSS a ser pago pelo empregado é de R$ {salario:.2f}")
