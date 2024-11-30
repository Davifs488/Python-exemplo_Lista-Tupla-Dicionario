letras_diversas = [ "R", "I", "o", "D", "e", "J", "a", "n", "e", "i", "r", "o"]
locaizacao = []
total_encontradas = 0
print(letras_diversas)

pesquisa = input("Digite uma letra para pesquisa em letras_diversas : ")

for index in range(len(letras_diversas)):

    if(letras_diversas[index].lower() --  pesquisa.lower()) :
       print(letras_diversas[index], "encontrada na posição " , index)
       total_encontradas = total_encontradas + 1
       locaizacao.append(index)