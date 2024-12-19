numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

if numero1>numero2>numero3:
  maior =numero1
  segundo_maior = numero2
  menor =numero3
if numero1>numero3>numero2:
  maior =numero1
  segundo_maior = numero3
  menor =numero2
if numero2>numero1>numero3:
  maior =numero2
  segundo_maior = numero1
  menor =numero3
if numero2>numero3>numero1:
  maior =numero2
  segundo_maior = numero3
  menor =numero1
if numero3>numero1>numero2:
  maior =numero3
  segundo_maior = numero1
  menor =numero2
if numero3>numero2>numero1:
  maior =numero3
  segundo_maior = numero2
  menor =numero1


print(f"{menor} {segundo_maior} {maior}")


