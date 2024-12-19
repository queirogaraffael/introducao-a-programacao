while True:
    numero = int(input())
    if numero==0:break
    for i in range(1,numero+1):
      if i == numero:
        print(i)
      else:
        print(i, end=" ")