def senha_segura(senha):
    if len(senha) < 4:
        return "Senha insegura"
    else:
        for i in range(1, len(senha) + 1):
            if i % 2 == 0:
                if int(senha[i - 1]) % 2 != 0:
                    return "Senha insegura"
            else:
                if int(senha[i - 1]) % 2 == 0:
                    return "Senha insegura"
        return "Senha segura"


assert senha_segura("12346") == "Senha insegura"
assert senha_segura("125638") == "Senha segura"
assert senha_segura("01234") == "Senha insegura"
assert senha_segura("3810") == "Senha segura"
assert senha_segura("1234567") == "Senha segura"
assert senha_segura("123") == "Senha insegura"