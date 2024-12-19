import math

raio = float(input())

area_circulo = math.pi * raio**2

l = raio * math.sqrt(2)

area_quadrado = l * l

resultado = area_circulo - area_quadrado

print(f"Área não comum: {resultado:.5f}")
