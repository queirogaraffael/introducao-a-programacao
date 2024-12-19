def dentro(elemento):
    if elemento == "de" or elemento == "da" or elemento == "do":
        return False
    else:
        return True


def cria_login(nome):
    nomes = nome.split()
    login = nomes[0].lower()
    for i in range(1, len(nomes)):
        if dentro(nomes[i]):
            login += nomes[i][0].lower()
    return login

nomes = []
logins = []

while True:
  nome = input()
  if nome == "fim":break
  nomes.append(nome)
  logins.append(cria_login(nome))

for i in range(len(nomes)):
  print(f"{nomes[i]}: {logins[i]}")


"""
assert cria_login("Matheus Gaudencio do Rego") == "matheusgr"
assert cria_login("Eliane Araujo") == "elianea"
assert cria_login("Dalton Serey Guerrero") == "daltonsg"
assert cria_login("Raffael Queiroga") == "raffaelq"
assert cria_login("Matheus Gaudencio Do Rego") == "matheusgdr"
assert cria_login("Debora da costa Da silva") == "deboracds"
"""