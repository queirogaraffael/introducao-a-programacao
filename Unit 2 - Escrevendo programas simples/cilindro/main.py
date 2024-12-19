print("Cálculo da Superfície de um Cilindro")
print("---")

diametro = float(input("Medida do diâmetro? "))
altura = float(input("Medida da altura? "))

raio = diametro/2

area = 2 * 3.14159 * raio**2 + 2 * 3.14159 * raio * altura

print("---")
print(f"Área calculada: {area:.2f}")