n = int(input())

paginas = n // 400

print(f"Serão necessárias {paginas} página(s) para visualizar os tweets.")

perdidos = ((n - 400*paginas)/n)*100

print(f"{perdidos:.1f}% dos tweets serão perdidos.")
