def histogram(s):
    d = dict()
    for letra in s:
        if letra not in d:
            d[letra] = 1
        else:
            d[letra] += 1
    return d


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


hist = histogram('parrot')
print(hist)
inverse = invert_dict(hist)

print(inverse)


chave e valor