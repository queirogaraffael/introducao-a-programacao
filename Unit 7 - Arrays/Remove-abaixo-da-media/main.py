def remove_abaixo_media(l):
  soma = 0

  for i in range(len(l)):
    soma+=l[i]

  media = soma /len(l)

  for i in range(len(l)-1, -1, -1):
    if l[i]<media:
      l.pop(i)


l1 = [1, 1, 1, 1]
remove_abaixo_media(l1)
assert l1 == [1, 1, 1, 1]

l1 = [1, 1, 1, -1, 1]
remove_abaixo_media(l1)
assert l1 == [1, 1, 1, 1]
