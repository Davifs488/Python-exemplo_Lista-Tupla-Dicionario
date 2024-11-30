#Tuplas são listas imutáveis ou fixas

sudeste = ("RJ", "ES", "SP", "MG") #criaçao da tupla
print(type(sudeste))
print(sudeste)
print(sudeste[0]) #RJ
print(sudeste[-1]) #MG (o ultim o)
print(sudeste[:2]) #RJ , ES (0,1,2 -> exceto o própio 2)
print(sudeste[1:3]) #ES, SP (1,2,3 -> exceto o própio 3)
print(sudeste[::2])  #RJ, SP (1  cada 2 posições)


print(len((sudeste))) # 4 -> Total de itens
print(sudeste.index("SP")) # 2
print(sudeste.count("SP")) # 1 -> Quantos intens SP exitem na trupa