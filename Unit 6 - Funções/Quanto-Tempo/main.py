def quanto_tempo(horario1, horario2):
    hora1 = horario1.split(":")
    hora2 = horario2.split(":")

    minutos1 = 60 * int(hora1[0]) + int(hora1[1])
    minutos2 = 60 * int(hora2[0]) + int(hora2[1])

    minutos_restante = minutos2 - minutos1

    horas = minutos_restante // 60

    minutos = minutos_restante - (horas * 60)

    resultado = str(horas) + " hora(s) e " + str(minutos) + " minuto(s)"

    return resultado


assert quanto_tempo("07:15", "09:18") == "2 hora(s) e 3 minuto(s)"
assert quanto_tempo("07:40", "08:15") == "0 hora(s) e 35 minuto(s)"
assert quanto_tempo("22:15", "23:05") == "0 hora(s) e 50 minuto(s)"
assert quanto_tempo("21:15", "23:05") == "1 hora(s) e 50 minuto(s)"
assert quanto_tempo("22:15", "23:05") == "0 hora(s) e 50 minuto(s)"
