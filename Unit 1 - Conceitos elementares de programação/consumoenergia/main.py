potencia = int(input()) # em watts
tempo = int(input()) # minutos

tempo_H = tempo /60
consumo = (potencia*tempo_H)/1000

print(f"{consumo:.1f} kWh")