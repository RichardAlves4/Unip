ano = int(input("Digite um ano: "))

decada = (ano // 10) * 10

if ano % 100 == 0:
    seculo = ano // 100
else:
    seculo = (ano // 100) + 1

print(f"O ano {ano} pertence à década de {decada} \nE ao século {seculo}")
