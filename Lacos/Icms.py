def calcular_icms(valor_produto, estado):
    icms_porcentagem = {
        "ES": 12,
        "TO": 20,
        "BA": 20.5
    }
    icms = icms_porcentagem.get(estado.upper(), 7)
    valor_imposto = valor_produto * (icms / 100)
    valor_total = valor_produto + valor_imposto
    return valor_imposto, valor_total

# Exemplo de uso
valor = float(input("Digite o valor do produto: "))
estado = input("Digite o estado (sigla): ")
imposto, total = calcular_icms(valor, estado)
print(f"ICMS: R$ {imposto:.2f}")
print(f"Total com imposto: R$ {total:.2f}")
