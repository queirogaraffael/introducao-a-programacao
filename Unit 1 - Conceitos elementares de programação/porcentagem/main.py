print("Análise da Turma")
print("===")

numero_aprovados = int(input("Número de aprovados? "))
numero_reprovados = int(input("Número de reprovados? "))

print("---")

total_alunos = numero_aprovados + numero_reprovados 

print(f"Total de alunos na turma: {total_alunos}")

aprovados = (numero_aprovados/total_alunos) * 100
reprovados = (numero_reprovados/total_alunos) * 100

print(f"Aprovados: {numero_aprovados} = {aprovados:.1f}%")
print(f"Reprovados: {numero_reprovados} = {reprovados:.1f}%")
