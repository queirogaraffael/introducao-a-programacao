def dentro(elemento,lista):
    for i in range(len(lista)):
      if elemento == lista[i]:
        return True
    return False


def sei_tocar_musica(musica, acordes):

    if len(musica)>len(acordes):
      return False
    else:
      for i in range(len(musica)):
        if not dentro(musica[i],acordes):
          return False
    return True
  

musica = ["a", "d", "dm"]
acordes = ["a", "d"]
assert not sei_tocar_musica(musica, acordes) == True

musica = ["a", "d"]
acordes = ["a", "bm", "d", "c"]
assert sei_tocar_musica(musica, acordes) == True

musica = ["a", "bm", "d", "c"]
acordes = ["a", "d"]
assert sei_tocar_musica(musica, acordes) == False

musica = ["a", "d", "dm"]
acordes = ["a", "d", "dm"]
assert sei_tocar_musica(musica, acordes) == True