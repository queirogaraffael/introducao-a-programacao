def calcula_conta(tabela):
  valor = 0 

  for i in range(1,len(tabela)):
      conta = (float(tabela[i][1]) * float(tabela[i][2]) * float(tabela[i][3]) * 0.28) /1000
      valor += conta

  resultado_final = f"R$ {valor:.2f}"

  return resultado_final



tabela = [["Equipamento", "Quantidade", "Tempo de Uso (horas)", "Potencia (Watts)"],
          ["AR-CONDICIONADO",    1,              240,               2000],
          ["COMPUTADOR",         2,              150,               180],
          ["TV",                 3,              150,               110]]

assert calcula_conta(tabela) == "R$ 163.38"


tabela = [["Equipamento", "Quantidade", "Tempo de Uso (horas)", "Potencia (Watts)"]]

assert calcula_conta(tabela) == "R$ 0.00"