def saudacao(nome):

    print(f"Seu nome e {nome}")


def calculo(n1, n2):
    soma = n1 + n2
    mult = n1 * n2
    print(f"Essa é a soma {soma}")
    print(f"Essa é a multiplicação {mult}")


def media(n1, n2, nome):
    med = ( n1 + n2 )/ 2

    print(f" A media é {med} e seu nome é {nome}")

nome_completo = input("Informe seu nome completo")
nota1 = float(input(" Informe sua nota 01 "))
nota2 = float(input(" Qual foi sua segunda nota " ))


media(nota1, nota2, nome_completo)


media(25, 7, "Amauri")
media(25, 9, "Moraiws")

calculo(5, 8)
calculo(12, 55)

saudacao("Elias")
saudacao("Sara")
saudacao("Karen")