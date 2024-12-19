def primeiro_menor(numero, numeros):
    indice = -1
    for i in range(len(numeros)):
        if numeros[i] < numero:
            return i
    return indice


def main():
    numeros = []
    valores = input().split()
    num = int(input())

    for i in range(len(valores)):
      numeros.append(int(valores[i]))

    indice = primeiro_menor(num, numeros)

    if indice != -1:
        print(f"primeiro menor que {num}: {numeros[indice]}")
    else:
      print(f"sem menores que {num}")


if __name__ == "__main__":
    main()


"""
$ python primmenor.py
7 5 3 9 11 8
4
primeiro menor que 4: 3

$ python primmenor.py
7 5 3 9 11 8
3
sem menores que 3

"""