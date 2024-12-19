lim = int(input())

soma = 0
a1 = 1
n = 1

while True:
    an = a1 * 2**(n - 1)
    soma += an
    if soma >= lim: break
    print(an)
    n += 1

1, 2, 4, 8, 16, 32, 64, 128
