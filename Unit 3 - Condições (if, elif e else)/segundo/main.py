numero1 = int(input())
numero2 = int(input())
numero3 = int(input())
numero4 = int(input())

print(f"Considerando os números {numero1}, {numero2}, {numero3} e {numero4}")

if numero1>numero2>numero3>numero4:
  segundo_menor = numero3
  segundo_maior = numero2
elif numero1>numero2>numero4>numero3:
  segundo_menor = numero4
  segundo_maior = numero2
elif numero1>numero3>numero2>numero4:
  segundo_menor = numero2
  segundo_maior = numero3
elif numero1>numero3>numero4>numero2:
  segundo_menor = numero4
  segundo_maior = numero3
elif numero1>numero4>numero3>numero2:
  segundo_menor = numero3
  segundo_maior = numero4
elif numero1>numero4>numero2>numero3:
  segundo_menor = numero2
  segundo_maior = numero4
elif numero2>numero1>numero3>numero4:
  segundo_menor = numero3
  segundo_maior = numero1
elif numero2>numero1>numero4>numero3:
  segundo_menor = numero4
  segundo_maior = numero1
elif numero2>numero3>numero1>numero4:
  segundo_menor = numero1
  segundo_maior = numero3
elif numero2>numero3>numero4>numero1:
  segundo_menor = numero4
  segundo_maior = numero3
elif numero2>numero4>numero3>numero1:
  segundo_menor = numero3
  segundo_maior = numero4
elif numero2>numero4>numero1>numero3:
  segundo_menor = numero1
  segundo_maior = numero4
elif numero3>numero2>numero1>numero4:
  segundo_menor = numero1
  segundo_maior = numero2
elif numero3>numero2>numero4>numero1:
  segundo_menor = numero4
  segundo_maior = numero2
elif numero3>numero1>numero2>numero4:
  segundo_menor = numero2
  segundo_maior = numero1
elif numero3>numero1>numero4>numero2:
  segundo_menor = numero4
  segundo_maior = numero1
elif numero3>numero4>numero1>numero2:
  segundo_menor = numero1
  segundo_maior = numero4
elif numero3>numero4>numero2>numero1:
  segundo_menor = numero2
  segundo_maior = numero4
elif numero4>numero2>numero3>numero1:
  segundo_menor = numero3
  segundo_maior = numero2
elif numero4>numero2>numero1>numero3:
  segundo_menor = numero1
  segundo_maior = numero2
elif numero4>numero3>numero2>numero1:
  segundo_menor = numero2
  segundo_maior = numero3
elif numero4>numero3>numero1>numero2:
  segundo_menor = numero1
  segundo_maior = numero3
elif numero4>numero1>numero3>numero2:
  segundo_menor = numero3
  segundo_maior = numero1
else:
  segundo_menor = numero2
  segundo_maior = numero1

print(f"O segundo menor número é {segundo_menor}")  
print(f"O segundo maior número é {segundo_maior}")
