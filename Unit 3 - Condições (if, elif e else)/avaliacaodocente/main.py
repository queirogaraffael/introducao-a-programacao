semestre = int(input())
ensino = float(input())
prod_intelec = float(input())
orientacao = float(input())
administrativa = float(input())


if semestre>=4:
  if ensino>= 320 and prod_intelec >=100 and orientacao>=20:
    media = (ensino+prod_intelec+orientacao+administrativa)/4
    if media>140:
      print("Promoção deferida. Parabéns!")
    else:
      print( "Promoção indeferida. Média insuficiente.")
  else:
    print("Promoção indeferida. Pontuação mínima não alcançada.")
else:
  print("Promoção indeferida. Número de semestres insuficiente.")



