while True:
    numero = input().split()
    x = int(numero[0])
    y = int(numero[1])
    if x == y: break
    if x > y:
        print("Decrescente")
    else:
        print("Crescente")
