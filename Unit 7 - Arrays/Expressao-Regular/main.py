def compara(str1, str2):
    controle = 0
    for i in range(len(str1)):
        if str2[-i - 1] == str1[-i - 1]:
            controle += 1
    if controle == len(str1):
        return True
    else:
        return False


def is_substring_expr(str1, str2):
    if len(str2)-1 <= len(str1):
        str2 = str2.split("*")
        primeira = str2[0]
        ultima = str2[1]
        if compara(primeira, str1[:len(primeira)]) == True and compara(
                ultima, str1):
            return True
    return False


assert is_substring_expr('oicarovoce', 'oi*voce') == True
assert is_substring_expr('oicvoce', 'oi*voce') == True
assert is_substring_expr('naoobaminiprog1', 'oba*prog1') == False
assert is_substring_expr('vocecaraoi', 'voce*oi') == True
assert is_substring_expr('voceeeeeeeeeeeeeecaraoiiiiiiiiiiiiiiii',
                         'voceee*oiiii') == False
assert is_substring_expr('vocecaraoi', 'voceeeeee*oiiiiiiii') == False
assert is_substring_expr('voceeeeeeeeeeeeeecaraooooooiiii',
                         'voceee*oiiii') == True
assert is_substring_expr('vocecaraoi', 'vocee*oiiii') == False
assert is_substring_expr('oivoce', 'oi*voce') == True
assert is_substring_expr('voceeooi', 'voce*oi') == True