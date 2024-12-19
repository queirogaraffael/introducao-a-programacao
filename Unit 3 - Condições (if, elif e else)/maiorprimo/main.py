numero = int(input())

if numero%7 ==0:
  K = numero/ 7
  print(f"7 * {K:.0f} = {numero}")
elif numero%5==0:
  K = numero/ 5
  print(f"5 * {K:.0f} = {numero}")
elif numero%3==0:
  K = numero/ 3
  print(f"3 * {K:.0f} = {numero}")
elif numero%2==0:
  K = numero/ 2
  print(f"2 * {K:.0f} = {numero}")
else:
  print(f"{numero} não tem fatores primos menores que 10")  


