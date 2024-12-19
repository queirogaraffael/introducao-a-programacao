salario_bruto = float(input())
horas_de_trabalho = float(input())

desconto_IR = salario_bruto * 0.11
desconto_INSS = salario_bruto *0.08
desconto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - desconto_INSS - desconto_IR - desconto_sindicato

hora_bruta = salario_bruto/horas_de_trabalho

hora_liquida = salario_liquido/horas_de_trabalho

print(f"Salário Bruto = {salario_bruto:.2f}")
print(f"Hora Bruta = {hora_bruta:.2f}")
print(f"Desconto IR = {desconto_IR:.2f}")
print(f"Desconto INSS = {desconto_INSS:.2f}")
print(f"Desconto Sindicato = {desconto_sindicato:.2f}")
print(f"Salário Líquido = {salario_liquido:.2f}")
print(f"Hora Líquida = {hora_liquida:.2f}")
