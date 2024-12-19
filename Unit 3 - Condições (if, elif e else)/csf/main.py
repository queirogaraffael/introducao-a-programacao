nota_enem = float(input())
creditos = int(input())

concluido = (creditos / 416) * 100

if 20 <= concluido <= 90 and nota_enem >= 600:
    print("Todas as condições satisfeitas.")
elif 20 <= concluido <= 90 and nota_enem < 600:
    print("Condição ENEM não satisfeita.")
elif (concluido < 20 or concluido > 90) and nota_enem >= 600:
    print("Condição CRÉDITOS não satisfeita.")
else:
    print("Nenhuma condição satisfeita.")
