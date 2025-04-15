valor = float(input("Informe o valor de sua prestação: "))

taxa = float(input("Informe a taxa referente a sua prestação: "))

tempo = int(input("informe quantos os messes vencidos: "))

prestacao = valor
prestacaoAtrazada = valor + (valor * (taxa/100) * tempo)

print(f"O valor inícial de sua prestação era de {prestacao} R$ com o atraso de {tempo} messes o valor a se pagar será de {prestacaoAtrazada} R$")