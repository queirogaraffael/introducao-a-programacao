unid_tijolo = float(input("Digite o preço da unidade do tijolo (Em reais): "))
alt_tijolo = float(input("Digite a altura do tijolo (Em metros): "))
comp_tijolo = float(input("Digite o comprimento do tijolo (Em metros): "))
alt_parede = float(input("Digite a altura das paredes (Em metros): "))
comp_parede = float(input("Digite o comprimento das paredes (Em metros): "))


num_tijolos_altura = alt_parede/ alt_tijolo
num_tijolos_largura = comp_parede / comp_tijolo

num_tijolos_total = num_tijolos_altura * num_tijolos_largura

orcamento = unid_tijolo * num_tijolos_total

print(f"O número total de tijolos é {num_tijolos_total:.1f} e o orçamento final é de R$ {orcamento:.1f}")
