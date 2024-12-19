nome = input()
hora_extra = float(input())
valor_salario_minimo = float(input())
valor_hora_extra = float(input())

salario_hora_extra = hora_extra * valor_hora_extra
salario_bruto = 4 * valor_salario_minimo + salario_hora_extra
desconto_inss = 0.12*salario_bruto
desconto_imposto_renda = 0.20*salario_bruto
salario_liquido = salario_bruto - desconto_imposto_renda - desconto_inss

print(f"O Salário Bruto de Antonio é de R$ {salario_bruto:.2f}")
print(f"O Salário Líquido de Antonio é de R$ {salario_liquido:.2f}")
