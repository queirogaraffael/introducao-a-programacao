def is_substring(str1, str2):
    if len(str2) <= len(str1):
        for i in range(len(str1) - len(str2) + 1):
            controle = 0
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    controle += 1
                    i += 1
                    if controle == len(str2):
                        return True
    return False


assert is_substring('boiada', 'oioioioioioi') == False
assert is_substring('boiada', 'oi') == True
assert is_substring('casorio', 'casa') == False
assert is_substring('boiada', 'boiada') == True
assert is_substring('casorio', 'caso') == True
assert is_substring('oi', 'boiada') == False
assert is_substring('casa', 'casorio') == False
assert is_substring('vidro', 'vidroso') == False
assert is_substring('casorio', 'casori') == True
assert is_substring('casorio', 'casarr') == False
assert is_substring('casorio', 'casarr') == False
assert is_substring('casorio', 'casorr') == False
assert is_substring('abccaso', 'caso') == True
assert is_substring('abccasa', 'caso') == False
assert is_substring('abccasaabc', 'caso') == False
