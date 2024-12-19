def eh_primo(numero):
    soma = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            soma += 1
    if soma == 2:
        return True
    else:
        return False


def divisores(numero):
    div = ""
    for i in range(1, numero + 1):
        if numero % i == 0:
            div += str(i) + " "
    numero1 = div.rstrip()
    return numero1


while True:
    entrada = input()
    if entrada == "": break
    numero = int(entrada)
    if eh_primo(numero):
        print(f"{numero}: primo")
    else:
        print(f"{numero}: {divisores(numero)} não é primo")
