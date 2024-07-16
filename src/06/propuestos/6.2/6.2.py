import zereginak

nireZereginak = zereginak.Tareas()

print(nireZereginak.erakutsi(), "\n---")

nireZereginak.sortu(2, "Eskatzak")
print(nireZereginak.erakutsi(), "\n---")

nireZereginak.ezabatu(2)
print(nireZereginak.erakutsi(), "\n---")

nireZereginak.sortu(66, "Irakurri")
print(nireZereginak.erakutsi(), "\n---")
nireZereginak.gorde()