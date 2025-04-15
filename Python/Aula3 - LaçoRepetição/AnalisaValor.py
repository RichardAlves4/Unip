valor = int(input("Informe um valor: "))

maiorValor = 0

menorValor = 10

somaValor = valor

for i in range(4):

    valor = int(input("Informe um valor: "))

    if valor > maiorValor:
        maiorValor = valor
    
    if valor < menorValor:
        menorValor = valor

    somaValor += valor

media = somaValor ** 5 

print(f"\nDados dos valores informedos \nMaior valor: {maiorValor} \nMenor valor: {menorValor} \nMédia: {media}" )