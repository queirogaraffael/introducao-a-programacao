abstencao = int(input())
a_favor = int(input())
contra = int(input())

total = abstencao + a_favor +contra

p_abstencao = (abstencao/total)*100
p_a_favor = (a_favor/total) * 100
p_contra = (contra/total)*100


print("Resultado da Votação")
print("")

print(f"{abstencao} abstenções ({p_abstencao:.2f}%)")
print(f"{a_favor} a favor ({p_a_favor:.2f}%)")
print(f"{contra} contra ({p_contra:.2f}%)")
