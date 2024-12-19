def indice(nome):
  alfabeto_morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
  for i in range(len(alfabeto_morse)):
    if nome == alfabeto_morse[i]:
      return i


def tradutor_morse(lista):
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    palavra = ''
    for i in range(len(lista)):
      posicao = indice(lista[i])
      palavra += str(alfabeto[posicao])
    return palavra


assert tradutor_morse(['.--.', '-.--', '-', '....', '---', '-.']) == 'python'
assert tradutor_morse(['.-.','.-','..-.','..-.','.-','.','.-..']) == 'raffael'