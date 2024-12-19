string_qualquer = input()
hora = int(input())

permitido = 6<hora<22
if string_qualquer == "" and permitido:
  print("Condomínio em Paz.")
else:
  print("Perturbação Detectada!")