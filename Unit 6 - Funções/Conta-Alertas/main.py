def conta_alertas_acude(medicoes):
  alarme = 0
  for i in range(len(medicoes)-1):
    if abs(medicoes[i]-medicoes[i+1]) < 10:
      if medicoes[i+1]<17:
        alarme+=1
  return alarme


medicoes = [50, 50, 50, 23, 21, 17, 15, 60, 65, 15, 15]
assert conta_alertas_acude(medicoes) == 2

medicoes = [50, 50, 50, 23, 21, 17, 15, 60, 65, 15, 15, 15]
assert conta_alertas_acude(medicoes) == 3

medicoes = [50, 50, 50, 23, 17, 17, 15, 25, 65, 15]
assert conta_alertas_acude(medicoes) == 1

medicoes = [50, 50, 50, 23, 17, 17, 15, 25, 65]
assert conta_alertas_acude(medicoes) == 1

medicoes = [50, 50, 50, 23, 17, 17, 15, 19, 15]
assert conta_alertas_acude(medicoes) == 2

medicoes = [50, 50, 50, 23, 17, 17, 15, 25, 15]
assert conta_alertas_acude(medicoes) == 1

medicoes = [50, 50, 50, 23, 17, 17, 17, 25, 17]
assert conta_alertas_acude(medicoes) == 0