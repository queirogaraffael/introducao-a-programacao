def soma_matrizes_esparsas(m1, m2):
  dicionario1 = m1[2]
  dicionario2 = m2[2]
  
    if dicionario1 in dicionario2:
      m1[chave] += m2[chave]
      return m1
    else:
      m1.append(m2[2])
      return m1

      
    




M1 = (120, 200, {(115, 64): -5})
M2 = (120, 200, {(20, 55): 5})

SOMA1 = soma_matrizes_esparsas(M1, M2)
print(SOMA1)
#assert SOMA1 == (120, 200, {(115, 64): -5, (20, 55): 5})