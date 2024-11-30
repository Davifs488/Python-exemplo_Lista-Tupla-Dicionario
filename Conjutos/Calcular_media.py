from exe_func_media import alunos


def calcular_media(notas):
    total_notas = 0
    for nota in notas:
        total_notas += nota
        media = total_notas / len(notas)
        return media




print("\nFazendo uso da funlçapo calcular_media e formatando a saida de dados :")
for aluno in alunos:
        nome = aluno["nome"]
        notas = aluno["notas"]
        media = calcular_media(notas)
        print(f"Nome: {nome} - NOtas: {notas} - Mádia: {media}")