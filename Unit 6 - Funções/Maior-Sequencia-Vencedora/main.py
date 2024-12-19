def maior_sequencia_vencedora(lista):
    if lista == []:
      return None, 0, None
    else:
      consecutivos, consecutivos_antigo = 0,0

      nome, nome_antigo = "", ""
      posicao_final = 0

      for i in range(len(lista)-1):
        if lista[i] != lista[i+1]:
          if consecutivos > consecutivos_antigo:
            consecutivos_antigo = consecutivos + 1
            nome_antigo = nome
            posicao_final = i + 1

          consecutivos = 0
        else:
          nome = lista[i]
          consecutivos+=1

      if consecutivos > consecutivos_antigo:
            consecutivos_antigo = consecutivos + 1
            nome_antigo = nome
            posicao_final = len(lista)

      posicao_inicial = posicao_final - consecutivos_antigo 

      return (nome_antigo,consecutivos_antigo, posicao_inicial)



campeoes = ["b", "ae", "edm", "c", "c", "c", "c", "c", "c", "t", "c", "b", "b", "b","c", "c", "c", "c", "b", "t"]
vazia = []
vencedores = ["b", "ae", "edm", "t", "c", "b", "b", "b", "c", "c", "c", "c", "b", "t","d", "d", "d", "d", "d", "d", "d"]
vencedores2 = ["c", "c", "c", "c", "c", "c", "b", "ae", "edm", "t", "c", "b", "b", "b","c", "c", "c", "c", "b", "t"]

vencedores3 = ["c", "c", "c", "c", "c", "c", "b", "ae", "edm", "t", "c", "b", "b", "b","c", "c", "c", "c", "b", "t","c", "c", "c", "c", "c", "c", "c"]

vencedores4 = ["c", "c", "c", "c", "c", "c", "b", "ae", "edm", "t", "c", "b", "b", "b","c", "c", "c", "c", "b", "t","c", "c", "c", "c", "c", "c"]

assert maior_sequencia_vencedora(campeoes) == ("c", 6, 3) 
assert maior_sequencia_vencedora(
    ["Palmeiras", "Flamengo", "Flamengo", "Grêmio"]) == ("Flamengo", 2, 1) 
assert maior_sequencia_vencedora(vazia) == (None, 0, None) 
assert maior_sequencia_vencedora(vencedores) == ("d", 7, 14) 
assert maior_sequencia_vencedora(vencedores2) == ("c", 6, 0) 
assert maior_sequencia_vencedora(vencedores3) == ("c", 6, 0)
assert maior_sequencia_vencedora(vencedores4) == ("c", 6, 0)