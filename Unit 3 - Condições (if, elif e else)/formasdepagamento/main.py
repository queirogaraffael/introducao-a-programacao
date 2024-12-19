area = float(input())
valor = float(input())
forma = input()

total = area * valor 

if forma == "vista":
  total_com_desconto = total * 0.8
  print(f"Total: R$ {total_com_desconto:.2f}")
elif forma == "2x":
  total_com_desconto = total * 0.9
  parcelas = total_com_desconto/2
  print(f"Total: R$ {total_com_desconto:.2f}. Parcelas: R$ {parcelas:.2f}")
else:
  total_com_desconto = total * 0.95
  parcelas = total_com_desconto/3
  print(f"Total: R$ {total_com_desconto:.2f}. Parcelas: R$ {parcelas:.2f}")
