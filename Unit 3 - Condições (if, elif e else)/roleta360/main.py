forca = int(input())

resto = forca%360

if 0<resto<90:
  print("Quadrante 1")
elif 90<resto<180:
  print("Quadrante 2")
elif 180<resto<270:
  print("Quadrante 3")
elif 270<resto<360:
  print("Quadrante 3")
else: 
  print("Sobre eixos")
