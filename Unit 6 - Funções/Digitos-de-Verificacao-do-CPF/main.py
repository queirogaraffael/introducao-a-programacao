def calcula_digitos_verificacao(cpf):
    string = list(cpf)

    digito1 = 10 * (
        int(string[8]) * 2 + int(string[7]) * 3 + int(string[6]) * 4 +
        int(string[5]) * 5 + int(string[4]) * 6 + int(string[3]) * 7 +
        int(string[2]) * 8 + int(string[1]) * 9 + int(string[0]) * 10) % 11

    if digito1 == 10:
        digito1 = 0

    digito2 = 10 * (digito1 * 2 + int(string[8]) * 3 + int(string[7]) * 4 +
                    int(string[6]) * 5 + int(string[5]) * 6 + int(string[4]) *
                    7 + int(string[3]) * 8 + int(string[2]) * 9 +
                    int(string[1]) * 10 + int(string[0]) * 11) % 11

    if digito2 == 10:
        digito2 = 0

    digito_final = str(digito1) + str(digito2)
    return digito_final


assert calcula_digitos_verificacao('307271694') == '32'

assert calcula_digitos_verificacao('209822544') == '07'

assert calcula_digitos_verificacao('647005191') == '00'

assert calcula_digitos_verificacao('421487991') == '00'
