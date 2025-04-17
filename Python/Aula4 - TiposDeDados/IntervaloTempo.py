from datetime import datetime

tempo_destino = int(input("Informe um valor em anos para subtrair do ano atual: "))

ano_atual = datetime.now().year

resultado = ano_atual - tempo_destino

print(f"Atualemnte estamos no ano de {ano_atual} o intervalo de tempo entre {ano_atual} e {tempo_destino} que foi o tempo escolhido é: {resultado}")