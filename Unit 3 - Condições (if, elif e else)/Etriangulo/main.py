A = int(input())
B = int(input())
C = int(input())

if (abs(B-C)<A<(B+C)) | (abs(A-C)<B<(A+C)) | (abs(A-B)<C<(A+B)) :
  perimetro = A + B + C
  print(f"triangulo valido. {perimetro}")
else:
  print("triangulo invalido.") 