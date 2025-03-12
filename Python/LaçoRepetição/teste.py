print("Números de 1 a 10, ignorando os números pares:")

for numero in range(1, 11):

    if numero % 2 == 0:

        continue # Pula o restante do código para números pares

    print(f"Número ímpar: {numero}")