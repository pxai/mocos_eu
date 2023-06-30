def zenbatzarekin_hasi(longitatea, zenbakia):
    zenbakiak = []
    for i in range(longitorea):
        zenbakiak.append(zenbakia)
    return zenbakiak

def zenbatzarekin_hasi1(longitadea, zenbakia): return [zenbakia] * longitadea

print(zenbatzarekin_hasi(10, 3))
print(zenbatzarekin_hasi1(10, 3))