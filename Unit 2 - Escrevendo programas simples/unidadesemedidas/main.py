metros = float(input())

centimetro = metros * 100

jardas = centimetro / 91.44
pes = 3 * centimetro / 91.44
polegadas = 36 * centimetro / 91.44

print(f"Jardas: {jardas:.3f} yd")
print(f"Pés: {pes:.3f} ft")
print(f"Polegadas: {polegadas:.3f} in")
""""
100
Jardas: 109.361 yd
Pés: 328.084 ft
Polegadas: 3937.008 in"""
