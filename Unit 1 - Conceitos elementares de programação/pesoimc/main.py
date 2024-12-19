peso = float(input())
altura = float(input())

imc_atual = peso/altura**2

ganho_perdido = 24.9 * altura**2 - peso 


print(f"IMC atual = {imc_atual:.2f}")
print(f"Peso a ser ganho/perdido = {ganho_perdido:.2f}")