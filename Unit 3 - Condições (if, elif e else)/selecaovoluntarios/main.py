nome1 = input()
nome2 = input()
nome3 = input()

nome11=nome1
nome22=nome2
nome33=nome3

nome1 = (f"{nome1:.1s}")    # pego apenas a primeira letra pra comparar
nome2 = (f"{nome2:.1s}")
nome3 = (f"{nome3:.1s}")

if nome1<nome2<nome3:
  print(f"{nome11} (1)")
elif nome1<nome3<nome2:
  print(f"{nome11} (1)")
elif nome1<nome2<=nome3:
  print(f"{nome11} (1)")
elif nome1<nome3<=nome2:
  print(f"{nome11} (1)")
elif nome2<nome1<nome3:
  print(f"{nome22} (1)")
elif nome2<nome3<nome1:
  print(f"{nome22} (1)")
elif nome2<nome1<=nome3:
  print(f"{nome22} (1)")
elif nome2<nome3<=nome1:
  print(f"{nome22} (1)")
elif nome3<nome1<nome2:
  print(f"{nome33} (1)")
elif nome3<nome2<nome1:
  print(f"{nome33} (1)")
elif nome3<nome1<=nome2:
  print(f"{nome33} (1)")
elif nome3<nome2<=nome1:
  print(f"{nome33} (1)")
elif nome1 == nome2 or nome1 == nome3:
    print(f'{nome11} (2)')
elif nome2 == nome3:
    print(f'{nome22} (2)')
else:
    print(f'{nome33} (2)')
