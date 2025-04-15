B = int(input("Informe a base: "))
E = int(input("Informe o expoente: "))

resultado = 1
for i in range(E):
    resultado *= B

print(f"A potênciação de {B}^{E} = {resultado}")