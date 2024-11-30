#Dicionários são como as listas dinamicas, só que não são
# indexados a partir do zero, sim plor chaves, definidas durante
# o cadastro dos valores.
#OBS: Cada item dentro de um dicionario é composto por uma chave e por um valor
'''
OBS:No momento de declaração:
.Listas dinâmicas utilizam colchetes[ ]
.Tuplas utilizam parênteses( )
.Dicionários utilizam chaves { }

'''

#Criação de um dicionário chamado verbos. Observe a utilização das { }
verbos = {
    "pular" : "elevar-se do chão por inpulso dos pés e das pernas",
    "cair" : "ir ao chão",
    "devolver" : "entregar ou enviar de volta"
}

print(verbos)
print(type(verbos))

print(verbos["cair"]) #ir ao chão