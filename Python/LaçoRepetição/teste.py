B = int(input("Digite a base: "))
E = int(input("Digite o expoente: "))

resultado = 1
for _ in range(E):
    resultado *= B

print(resultado)