carro = {
    "fabricante" : "VW",
    "modelo" : "Fusca",
    "cor" : "Verde",
    "ano" : 1975,
    "donos" : ["João", " José", "Maria"]
}

#OBS: Dentro do dicionairo carro, "donos" possui contudso de listr dinamica

print(carro)
print(carro["modelo"]) # Fusca


print(carro["donos"])
carro["donos"].append("Maria") #Adiciona um item a lista donos.
print(carro["donos"])
print(carro["donos"][1] ) # Jossé

carro['KM'] = 115000 # Adiciona uma chave/valor ao final do dicionario
print(carro)

carro['KM'] = 173000 # Modifica o valor de uma chave já existente
print(carro)

carro.update({"cor" : "Amarelo"}) # Modifica o valor de uma chave
print(carro)

del carro["KM"] # Remove a chave KM
print(carro)

removido = carro.pop("cor") # Remove a chave e o valor correspondente
print(carro)
print(removido)