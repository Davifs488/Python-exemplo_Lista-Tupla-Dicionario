mensagens = [
    "Olá Mundo",
    "Python é melhor que java ",
    "Na verdade tudo depende do Banco de Dados",
    "Alguêm aqui faloou em programação No_code ? "

]

#Var mensagem recebe um item de  mensagens a cada ciclo de repetição
for mensagem in mensagens:
    print(mensagem)


#A cada ciclo de repetição a var indece recebe o índice do item e a
#var indice recebe o índice do intem e a var mensagem recebe o conteudo
#do intem de mensgens
for indice, mensagem in enumerate(mensagens):
    print(f"{indice} - {mensagem}")