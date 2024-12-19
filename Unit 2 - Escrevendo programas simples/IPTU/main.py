area_construida = float(input("Área construída? "))
aliquota = float(input("Alíquota? "))

valor_iptu = 35.00 + area_construida * aliquota

quota_unica = valor_iptu*0.75
quota_6 = valor_iptu*0.95
parcela6 = quota_6/ 6
parcela10 = valor_iptu/10

print(f"IPTU: R$ {valor_iptu:.2f}")

print("\nPagamento:")
print(f"1. Quota única. R$ {quota_unica:.2f}")
print(f"2. Em 6 parcelas. Total: R$ {quota_6:.2f}")
print(f"   6 x R$ {parcela6:.2f}")
print(f"3. Em 10 parcelas. Total: R$ {valor_iptu:.2f}")
print(f"   10 x R$ {parcela10:.2f}")
