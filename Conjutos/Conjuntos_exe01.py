#Conjutos(sets), são listas Não INDEXADAS.
'''
Também são declarados utilizando chaves { }
como os dicionarios, mas não possuem a chaves
de indecação para cada item. Somente o valor de cada item'''

nomes = {"João" , "Maria" , "Pedro" , " José" , "Ana"}
print(type(nomes))
print(nomes)

nomes.add("Jorge")
print(nomes)

nomes.remove("Jorge")
print(nomes)

nomes.add("Maria") # Não consegue adicionar item repetido
print(nomes)