cre = float(input())
meses = int(input())
nota_entrevista = float(input())


if cre<7.0 and meses <6:
  print("Candidato eliminado. CRE e experiência abaixo do limite.")
elif cre <7.0:
  print("Candidato eliminado. CRE abaixo do limite.")
elif meses <6:
  print("Candidato eliminado. Experiência abaixo do limite.")
elif nota_entrevista>3:
  print("Candidato aprovado.")
else:
  print("Candidato classificado.")
