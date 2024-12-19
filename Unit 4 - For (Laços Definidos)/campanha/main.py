pontos_em_casa_a_favor, pontos_em_casa_contra = 0, 0
pontos_fora_a_favor, pontos_fora_contra = 0, 0

vitoria1, derrota1, empate1 = 0, 0, 0
vitoria2, derrota2, empate2 = 0, 0, 0


def venceu_empate_derrota(ponto_campinense, ponto_adversario):
    vitoriaa, derrotaa, empatee = 0, 0, 0

    if ponto_campinense > ponto_adversario:
        vitoriaa += 1
    elif ponto_campinense < ponto_adversario:
        derrotaa += 1
    else:
        empatee += 1

    resultado = [vitoriaa, derrotaa, empatee]
    return resultado


for i in range(10):
    resultado = list(input())
    if resultado[5] == "c":
        pontos_em_casa_a_favor += int(resultado[0])
        pontos_em_casa_contra += int(resultado[2])
        resultado_comparacao = venceu_empate_derrota(int(resultado[0]),
                                                     int(resultado[2]))
        vitoria1 += int(resultado_comparacao[0])
        derrota1 += int(resultado_comparacao[1])
        empate1 += int(resultado_comparacao[2])
    else:
        pontos_fora_a_favor += int(resultado[2])
        pontos_fora_contra += int(resultado[0])
        resultado_comparacao = venceu_empate_derrota(int(resultado[2]),
                                                     int(resultado[0]))
        vitoria2 += int(resultado_comparacao[0])
        derrota2 += int(resultado_comparacao[1])
        empate2 += int(resultado_comparacao[2])

pontos = pontos_em_casa_a_favor + pontos_fora_a_favor
pontos_adversario = pontos_em_casa_contra + pontos_fora_contra
saldo = pontos - pontos_adversario
pontos1 = vitoria1 * 3 + vitoria2 * 3 + empate1 + empate2
pontos_em_casa = vitoria1 * 3 + empate1
ponto_fora = vitoria2 * 3 + empate2
vitoria = vitoria1 + vitoria2
empate = empate1 + empate2
derrota = derrota1 + derrota2

print(f"{vitoria}v, {empate}e, {derrota}d")
print(f"pontos: {pontos1}")
print(f"saldo: {saldo} ({pontos} pro, {pontos_adversario} contra)")
print(f"pontos em casa: {pontos_em_casa}")
print(f"pontos fora: {ponto_fora}")