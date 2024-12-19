voltagem = []
resistencia = []
corrente = []

for i in range(3):
    voltagem.append(float(input()))
    resistencia.append(float(input()))
    corrente.append(float(voltagem[i] / resistencia[i]))

if corrente[0] > corrente[1] >= corrente[2] or corrente[0] > corrente[
        2] >= corrente[1]:
    maior_corrente = corrente[0]
    controle = 1
elif corrente[1] > corrente[0] >= corrente[2] or corrente[1] > corrente[
        2] >= corrente[0]:
    maior_corrente = corrente[1]
    controle = 2
elif corrente[2] > corrente[0] >= corrente[1] or corrente[2] > corrente[
        1] >= corrente[0]:
    maior_corrente = corrente[2]
    controle = 3
elif corrente[0] == corrente[1] == corrente[2]:
    maior_corrente = corrente[0]
    controle = 1
elif corrente[1] == corrente[2] and corrente[1] > corrente[0]:
    maior_corrente = corrente[1]
    controle = 2
elif corrente[0] == corrente[1] and corrente[0] > corrente[2]:
    maior_corrente = corrente[0]
    controle = 1
else:
    maior_corrente = corrente[0]
    controle = 1

print(f"condutor com maior corrente: {controle}")

if maior_corrente >= 1:
    print(f"maior corrente: {maior_corrente:.2f} A")
elif maior_corrente < 0.001:
    resultado = maior_corrente * 1000000
    print(f"maior corrente: {resultado:.2f} µA")
else:
    resultado = maior_corrente * 1000
    print(f"maior corrente: {resultado:.2f} mA")