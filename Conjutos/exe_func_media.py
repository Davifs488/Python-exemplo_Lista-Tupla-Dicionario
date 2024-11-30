'''
Temos uma lista dinãmica onde cada item ~´e um
dicionario, em cada dicionario esta o nome e as notas de alunos,
porem, as notas estão dipostas em listas dinaicas detro do dicionario
'''

alunos = [
    {"nome" : "Rafael" , " notas" : [8, 9, 10]},
    {"nome" : "Aline" , "notas" : [5, 7, 6]},
    {"nome" : "Marcos" , "notas" : [3, 4, 5, 6]},
]

print("\n Exibindo cada item do dicionario ")
for aluno in alunos:
    print(aluno)



print(("\nEXbindo os items do dicionario com uma melhor manipulação de dados: "))
for aluno in alunos:
    print(f"Aluno: {aluno['nome']} - Notas: {aluno['notas']}")
