N = int(input("Informe o primeiro número: "))

M = int(input("Informe o segundo número: "))

resultado = 0

for i in range(M):

    resultado += N

print(f"A multiplicação {N}*{M} é igual a: {resultado}")