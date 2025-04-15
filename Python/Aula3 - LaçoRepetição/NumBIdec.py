numBi = int(input("Informe um número binário: "))

potencia = 0

acumulador = 0

while numBi > 0:
    
    fimDig = numBi % 10
    acumulador += fimDig * (2 ** potencia)
    numBi //= 10
    potencia += 1

print(F"\nA conversão do binário {numBi} para decimal é: \n{acumulador}")