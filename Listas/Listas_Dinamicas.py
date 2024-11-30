frutas = ["maçã", "Uva", "Banana" , "Manga" , "Laranja" , "Limão"]

print(frutas)
print(type(frutas))
print("Conteúdo do indice 1: " , frutas[1])
print("Total de frutas armazenadas : " , len(frutas))
print("Temos Manga ?" , "Manga" in frutas)
print("Temos Morango ? " , "Morango" in frutas)


#Adiciona ao final da lista
frutas.append("Morango")
print("\n" , frutas)
print("Temos Morango ? " , "Morango" in frutas)
print("Indice para Laranja em frutas : " , frutas.index("Laranja"))


#Remove da lista o item selecionado
frutas.remove("Uva")
print("\n" , frutas)
print(" Indice para  Laranja em frutas : " , frutas.index("Laranja"))


#Remove da lista o item do indice
del frutas[4]
print("\n Quem foi removido ? ")
print(frutas)

#Adiciona o item na posição apontada
frutas.insert(2, "Abacaxi")
print(frutas)

#Altera o valor  na posição apontada (não cria nova posição)
frutas[3] = "Acerola"
print(frutas)

print("\n" , frutas)
print(f" Total de itens no list : { len(frutas)}")

#Inverte a ordem dos itens da llista dinamica
frutas.reverse()
print(frutas)

#Coloca os itens da lista dinãmica em ordem alfbética
frutas.sort()
print(frutas)