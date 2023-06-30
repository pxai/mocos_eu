def positibo (balioa):
    if balioa < 0:
        return -balioa

    return balioa


def potentzia (balioa1, balioa2):
    return balioa1 ** balioa2

print(positibo(-1))
print(potentzia(2, 3))
print(potentzia(positibo(2), positibo(4)))
potentzia(positibo(-5), positibo(4))