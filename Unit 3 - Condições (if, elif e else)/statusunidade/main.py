quantidade = int(input())

if quantidade==1:
    nota1 = float(input())
    print(f"{nota1:.1f}")
    print('Aluno ainda não aprovado na unidade.')
elif quantidade==2:
    nota1 = float(input())
    nota2 = float(input())
    media = ((nota1+nota2)/2)
    print(f"{media:.1f}")
    if media >=6.0:
      print('Aluno aprovado na unidade')
    else:
      print("Aluno ainda não aprovado na unidade")
elif quantidade==3:
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    media = ((nota1+nota2+nota3)/3) - 0.5
    print(f"{media:.1f}")
    if media >=6.0:
      print('Aluno aprovado na unidade')
    else:
      print("Aluno ainda não aprovado na unidade")
else:
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    nota4 = float(input())
    media = ((nota1+nota2+nota3+nota4)/4) - 0.5
    print(f"{media:.1f}")
    if media >=6.0:
      print('Aluno aprovado na unidade')
    else:
      print("Aluno ainda não aprovado na unidade")
