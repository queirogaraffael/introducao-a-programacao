nota1_candidato1 = float(input())
nota2_candidato1 = float(input())
nota3_candidato1 = float(input())
idade1 = float(input())

nota1_candidato2 = float(input())
nota2_candidato2 = float(input())
nota3_candidato2 = float(input())
idade2 = float(input())


media1 = 0.3*nota1_candidato1 + 0.4*nota2_candidato1 + 0.3*nota3_candidato1
media2 = 0.3*nota1_candidato2 + 0.4*nota2_candidato2 + 0.3*nota3_candidato2

if media1>media2:
  print(f"O primeiro candidato foi aprovado com média {media1:.1f}.")
elif media2>media1:
  print(f"O segundo candidato foi aprovado com média {media2:.1f}.")
elif media1==media2 and idade1>idade2:
  print(f"O primeiro candidato foi aprovado com média {media1:.1f}.")
elif media1==media2 and idade1<idade2:
  print(f"O segundo candidato foi aprovado com média {media2:.1f}.")
else:
  print("Empate.")
