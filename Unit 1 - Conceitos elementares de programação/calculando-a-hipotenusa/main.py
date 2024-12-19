cateto1 = float(input("Cateto 1? "))
cateto2 = float(input("Cateto 2? "))

hipotenusa = cateto1 ** 2 + cateto2 ** 2

hipotenusaReal = hipotenusa ** 0.5 

print("Hipotenusa: {:.2f}".format(hipotenusaReal))